from sast_escaner.analyzers.ast_analyzer import ASTAnalyzer
from sast_escaner.analyzers.regex_analyzer import RegexAnalyzer

from sast_escaner.core.rule_engine import RuleEngine

from sast_escaner.report.report_generation import ReportGenerator


def main():

    file_path = input("Ingrese la ruta del archivo Python: ")

    # ------------------------------
    # Analizadores
    # ------------------------------

    ast_results = ASTAnalyzer().analyze(file_path)

    regex_results = RegexAnalyzer().analyze(file_path)

    findings = ast_results + regex_results

    # ------------------------------
    # Motor de reglas
    # ------------------------------

    engine = RuleEngine()

    results = engine.evaluate(findings)

    # ------------------------------
    # Reporte
    # ------------------------------

    ReportGenerator().generate(results)


if __name__ == "__main__":

    main()