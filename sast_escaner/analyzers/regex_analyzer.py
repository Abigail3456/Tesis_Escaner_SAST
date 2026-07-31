"""
=========================================================
Regex Analyzer
---------------------------------------------------------
Este módulo implementa el análisis basado en expresiones
regulares para detectar vulnerabilidades relacionadas con
credenciales o información sensible almacenada dentro del
código fuente.

Responsabilidad:
    - Leer el archivo.
    - Buscar patrones mediante expresiones regulares.
    - Generar objetos Finding.

El módulo NO:
    - Asigna severidades.
    - Genera reportes.
    - Clasifica vulnerabilidades.

Esas responsabilidades pertenecen al Rule Engine.
=========================================================
"""

import re

from sast_escaner.core.finding import Finding


class RegexAnalyzer:

    def __init__(self):
        """
        Inicializa el analizador.
        """

        self.findings = []
        self.file = ""

        # -------------------------------------------------
        # Catálogo de expresiones regulares
        #
        # La llave corresponde al Rule ID definido en
        # default_rules.py
        # -------------------------------------------------

        self.patterns = {

            # Contraseñas hardcodeadas
            "R-05": re.compile(
                r"(password|passwd|pwd)\s*=\s*['\"].+['\"]",
                re.IGNORECASE
            ),

            # API Keys
            "R-06": re.compile(
                r"(api[_-]?key)\s*=\s*['\"].+['\"]",
                re.IGNORECASE
            ),

            # Tokens
            "R-07": re.compile(
                r"(token)\s*=\s*['\"].+['\"]",
                re.IGNORECASE
            ),

            # Secrets
            "R-08": re.compile(
                r"(secret)\s*=\s*['\"].+['\"]",
                re.IGNORECASE
            )

        }

    # =====================================================
    # Método principal
    # =====================================================

    def analyze(self, file_path):
        """
        Analiza un archivo utilizando expresiones regulares.

        Parámetros:
            file_path (str)

        Retorna:
            list[Finding]
        """

        self.findings = []
        self.file = file_path

        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        self._scan_patterns(lines)

        return self.findings

    # =====================================================
    # Escaneo de patrones
    # =====================================================

    def _scan_patterns(self, lines):
        """
        Recorre todas las líneas del archivo y aplica todas
        las expresiones regulares definidas.
        """

        for line_number, line in enumerate(lines, start=1):

            for rule_id, pattern in self.patterns.items():

                if pattern.search(line):

                    self._add_finding(
                        rule_id,
                        line_number,
                        line
                    )

    # =====================================================
    # Crear Finding
    # =====================================================

    def _add_finding(self, rule_id, line_number, code):
        """
        Agrega un hallazgo encontrado durante el análisis.
        """

        self.findings.append(

            Finding(

                rule_id=rule_id,

                line=line_number,

                code=code.strip(),

                file=self.file

            )

        )