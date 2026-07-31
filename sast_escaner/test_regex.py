from sast_escaner.analyzers.ast_analyzer import ASTAnalyzer
from sast_escaner.analyzers.regex_analyzer import RegexAnalyzer
from sast_escaner.core.rule_engine import RuleEngine

# Analizador
analyzer = RegexAnalyzer()

findings = analyzer.analyze("sast_escaner/tests/vulnerable3.py")

# Motor
engine = RuleEngine()

results = engine.evaluate(findings)

# Mostrar resultados

for result in results:

    print(result)