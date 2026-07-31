from dataclasses import dataclass

@dataclass
class Finding:

    rule_id: str

    line: int

    code: str

    file: str
