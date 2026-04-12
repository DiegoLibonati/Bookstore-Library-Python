import logging

import pytest

from lend_book.configs.logger_config import setup_logger


class TestSetupLogger:
    @pytest.mark.unit
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-instance")
        assert isinstance(logger, logging.Logger)

    @pytest.mark.unit
    def test_logger_name_matches_argument(self) -> None:
        logger: logging.Logger = setup_logger("my-test-logger")
        assert logger.name == "my-test-logger"

    @pytest.mark.unit
    def test_logger_has_handlers(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-handlers")
        assert len(logger.handlers) > 0

    @pytest.mark.unit
    def test_default_name_returns_logger(self) -> None:
        logger: logging.Logger = setup_logger()
        assert isinstance(logger, logging.Logger)

    @pytest.mark.unit
    def test_same_name_returns_same_logger(self) -> None:
        logger_a: logging.Logger = setup_logger("shared-logger")
        logger_b: logging.Logger = setup_logger("shared-logger")
        assert logger_a is logger_b

    @pytest.mark.unit
    def test_same_name_does_not_duplicate_handlers(self) -> None:
        logger: logging.Logger = setup_logger("no-duplicate-handlers")
        initial_count: int = len(logger.handlers)
        setup_logger("no-duplicate-handlers")
        assert len(logger.handlers) == initial_count

    @pytest.mark.unit
    def test_logger_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-level")
        assert logger.level == logging.DEBUG

    @pytest.mark.unit
    def test_different_names_return_different_loggers(self) -> None:
        logger_a: logging.Logger = setup_logger("logger-alpha")
        logger_b: logging.Logger = setup_logger("logger-beta")
        assert logger_a is not logger_b
