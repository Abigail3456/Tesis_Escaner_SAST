from dataclasses import dataclass

@dataclass
class Rule:
    id: str
    name: str
    method: str          # AST o REGEX
    pattern: str
    severity: str
    description: str
    recommendation: str