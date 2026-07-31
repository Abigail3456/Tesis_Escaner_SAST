from sast_escaner.core.finding import Finding
from sast_escaner.core.rule_engine import RuleEngine

engine = RuleEngine()

findings = [

    Finding(
        rule_id="R-01",
        line=18,
        code="eval(input())",
        file="login.py"
    ),

    Finding(
        rule_id="R-04",
        line=25,
        code='password="1234"',
        file="config.py"
    )

]

results = engine.evaluate(findings)

for r in results:

    print(r)