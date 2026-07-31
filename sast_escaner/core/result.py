from dataclasses import dataclass

@dataclass
class Result:

    id: str

    name: str

    severity: str

    description: str

    recommendation: str

    file: str

    line: int

    code: str