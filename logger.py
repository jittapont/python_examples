import json
import logging
import logging.config
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional


class Logger(ABC):
    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def warning(self):
        pass

    @abstractmethod
    def error(self):
        pass

    @abstractmethod
    def exception(self):
        pass


class DefaultLogger(Logger):
    def __init__(self, logger_name: Optional[str] = None) -> None:
        if logger_name is None:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logging.getLogger(logger_name)

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg)

    def exception(self, msg: str) -> None:
        self.logger.exception(msg)


class CustomLogger(Logger):
    def __init__(
        self,
        log_file_name: str,
        log_folder: Path,
        config: Dict[str, Any],
        logger_name: str,
    ) -> None:
        if not log_folder.exists():
            log_folder.mkdir()
        config["handlers"]["file_handler"]["filename"] = str(
            log_folder
            / config["handlers"]["file_handler"]["filename"].format(
                filename=log_file_name
            )
        )
        logging.config.dictConfig(config)
        self.logger = logging.getLogger(logger_name)

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg)

    def exception(self, msg: str) -> None:
        self.logger.exception(msg)


class FakeLogger(Logger):
    def __init__(self, logger_name: Optional[str] = None) -> None:
        if logger_name is None:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logging.getLogger(logger_name)

    def debug(self, msg: str) -> None:
        print(f"Fake logger debug method is called with {repr(msg)}")

    def info(self, msg: str) -> None:
        print(f"Fake logger info method is called with {repr(msg)}")

    def warning(self, msg: str) -> None:
        print(f"Fake logger warning method is called with {repr(msg)}")

    def error(self, msg: str) -> None:
        print(f"Fake logger error method is called with {repr(msg)}")

    def exception(self, msg: str) -> None:
        print(f"Fake logger exception method is called with {repr(msg)}")
