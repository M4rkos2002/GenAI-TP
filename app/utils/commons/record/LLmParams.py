from dataclasses import dataclass, field

@dataclass
class LLmParams:
    temperature: float = field(default=0.2)
    max_tokens: int = field(default=4096)
    top_p: float = field(default=1.0)
    frequency_penalty: float = field(default=0.0)
    presence_penalty: float = field(default=0.0)
    stop: list[str] = field(default_factory=list)

    def __post_init__(self):
        """
        Post initialization of data class. Verifies if values are in field.
        :raise: ValueError
        :return: void
        """
        if not (0.0 <= self.temperature <= 1.0):
            raise ValueError(f"Temperature must be between 0 and 1, got {self.temperature}")

        if self.max_tokens <= 0:
            raise ValueError(f"max_tokens must be greater than 0, got {self.max_tokens}")

        if not (0.0 <= self.top_p <= 1.0):
            raise ValueError(f"top_p must be between 0 and 1, got {self.top_p}")

        if not (-2.0 <= self.frequency_penalty <= 2.0):
            raise ValueError(f"frequency_penalty must be between -2 and 2, got {self.frequency_penalty}")

        if not (-2.0 <= self.presence_penalty <= 2.0):
            raise ValueError(f"presence_penalty must be between -2 and 2, got {self.presence_penalty}")
