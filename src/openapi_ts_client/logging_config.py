"""Logging configuration for the openapi-ts-client package."""

import logging
import sys
from typing import Optional

# Package logger name
LOGGER_NAME = "openapi_ts_client"

# Verbose format with all details
VERBOSE_FORMAT = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(module)s:%(funcName)s:%(lineno)d | %(message)s"
)

# Date format for timestamps
DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


def setup_logging(level: int = logging.DEBUG) -> logging.Logger:
    """
    Set up verbose logging for the openapi-ts-client package.

    This configures a logger with detailed output including:
    - Timestamp with milliseconds
    - Log level
    - Logger name
    - Module, function name, and line number
    - The log message

    Args:
        level: The logging level to use. Defaults to DEBUG for maximum verbosity.

    Returns:
        The configured logger instance.
    """
    logger = logging.getLogger(LOGGER_NAME)

    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger

    logger.setLevel(level)

    # Create console handler with verbose formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    # Create formatter with verbose format
    formatter = logging.Formatter(fmt=VERBOSE_FORMAT, datefmt=DATE_FORMAT)
    console_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(console_handler)

    # Prevent propagation to root logger
    logger.propagate = False

    logger.debug("Logger initialized with verbose output")
    logger.debug(f"Log level set to: {logging.getLevelName(level)}")
    logger.debug(f"Log format: {VERBOSE_FORMAT}")

    return logger


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance for the package.

    Args:
        name: Optional sub-logger name. If provided, returns a child logger.

    Returns:
        The logger instance.
    """
    if name:
        return logging.getLogger(f"{LOGGER_NAME}.{name}")
    return logging.getLogger(LOGGER_NAME)
