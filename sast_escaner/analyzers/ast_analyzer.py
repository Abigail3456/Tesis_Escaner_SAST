import ast
from platform import node

from sast_escaner.core.finding import Finding


class ASTAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.findings = []
        self.file = ""

    def analyze(self, file_path):
        """
        Analiza un archivo Python y devuelve una lista de Findings.
        """

        self.findings = []
        self.file = file_path

        with open(file_path, "r", encoding="utf-8") as file:
            source = file.read()

        tree = ast.parse(source)

        self.visit(tree)

        return self.findings

    # ======================================================
    # Recorrido principal del AST
    # ======================================================

    def visit_Call(self, node):

        self._check_direct_calls(node)

        self._check_module_calls(node)

        self._check_subprocess(node)

        self.generic_visit(node)

    # ======================================================
    # Funciones auxiliares
    # ======================================================

    def _add_finding(self, rule_id, node, code):

        self.findings.append(
            Finding(
                rule_id=rule_id,
                line=node.lineno,
                code=code,
                file=self.file
            )
        )

    # ======================================================
    # 1. Llamadas directas
    # eval()
    # exec()
    # ======================================================

    def _check_direct_calls(self, node):

        if not isinstance(node.func, ast.Name):
            return

        direct_rules = {
            "eval": "R-01",
            "exec": "R-02",
        }

        rule = direct_rules.get(node.func.id)

        if rule:
            self._add_finding(
                rule,
                node,
                f"{node.func.id}()"
            )

    # ======================================================
    # 2. Llamadas a funciones de módulos
    # os.system()
    # ======================================================

    def _check_module_calls(self, node):

        if not isinstance(node.func, ast.Attribute):
            return

        if not isinstance(node.func.value, ast.Name):
            return

        module = node.func.value.id
        function = node.func.attr

        module_rules = {

            ("os", "system"): "R-03",

        }

        rule = module_rules.get((module, function))

        if rule:

            self._add_finding(
                rule,
                node,
                f"{module}.{function}()"
            )

    # ======================================================
    # 3. Casos especiales
    # subprocess(..., shell=True)
    # ======================================================

    def _check_subprocess(self, node):

        if not isinstance(node.func, ast.Attribute):
            return

        if not isinstance(node.func.value, ast.Name):
            return

        module = node.func.value.id

        function = node.func.attr

        if module != "subprocess":
            return

        valid_functions = {

            "run",
            "call",
            "Popen"

        }

        if function not in valid_functions:
            return

        for keyword in node.keywords:

            if keyword.arg == "shell":

                if (
                    isinstance(keyword.value, ast.Constant)
                    and keyword.value.value is True
                ):

                    self._add_finding(
                        "R-04",
                        node,
                        f"subprocess.{function}(shell=True)"
                    )