"""
Logger Configuration Module
Centralized logging setup for LUCIUS components
"""

import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)


def setup_logger(name):
    """
    Setup a logger with both file and console handlers.
    
    Args:
        name (str): Logger name (usually module name)
        
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)

    # Only configure if not already configured
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # Create formatters
    detailed_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_formatter = logging.Formatter(
        "%(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )

    # File handler (detailed logs)
    log_filename = os.path.join(LOGS_DIR, f"lucius_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)

    # Console handler (less verbose)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
