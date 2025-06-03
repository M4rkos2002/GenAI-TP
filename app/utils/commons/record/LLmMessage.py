from dataclasses import dataclass

@dataclass
class LLmMessage:
    role: str
    message: str
