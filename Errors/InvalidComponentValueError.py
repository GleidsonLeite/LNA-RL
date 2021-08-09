class InvalidComponentValueError(Exception):
    def __init__(self, value: float, message: str) -> None:
        super().__init__()
        self.value = value
        self.message = message

    def __str__(self) -> str:
        return f"Error when setting component value: {self.value} -> {self.message}"
