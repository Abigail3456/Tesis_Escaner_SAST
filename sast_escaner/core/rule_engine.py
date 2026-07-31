from sast_escaner.core.result import Result
from .result import Result
from ..rules.default_rules import DEFAULT_RULES

class RuleEngine:

    def __init__(self):

        self.rules = {
            rule.id: rule
            for rule in DEFAULT_RULES
        }

    def evaluate(self, findings):

        results = []

        for finding in findings:

            rule = self.rules.get(finding.rule_id)

            if rule:

                results.append(
                    Result(
                    id=rule.id,
                    name=rule.name,
                    severity=rule.severity,
                    description=rule.description,
                    recommendation=rule.recommendation,
                    file=finding.file,
                    line=finding.line,
                    code=finding.code
                    )
                )

        return results