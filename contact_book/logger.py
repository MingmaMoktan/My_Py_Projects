from enum import Enum

class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

class Logger:
    """Handles logging for different levels of events."""
    def __init__(self, log_file: str, level: LogLevel = LogLevel.INFO):
        self.log_file = log_file
        self.level = level

    def _log(self, message: str, level: LogLevel) -> None:
        """This logs a message if the log level is sufficient."""
        if level.value >= self.level.value:
            print(message)

    def debug(self, message: str) -> None:
        self._log(message, LogLevel.DEBUG)

    def info(self, message: str) -> None:
        self._log(message, LogLevel.INFO)

    def warning(self, message: str) -> None:
        self._log(message, LogLevel.WARNING)

    def error(self, message: str) -> None:
        self._log(message, LogLevel.ERROR)
