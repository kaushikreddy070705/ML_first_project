import logging
from logging.handlers import RotatingFileHandler

from app.config import LOG_FILE, LOG_LEVEL


# ============================================================
# LOG FORMAT
# ============================================================

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)


# ============================================================
# CONFIGURE LOGGING
# ============================================================

def setup_logging():

    log_level = getattr(
        logging,
        LOG_LEVEL,
        logging.INFO
    )


    # --------------------------------------------------------
    # FILE HANDLER
    # --------------------------------------------------------

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )


    # --------------------------------------------------------
    # CONSOLE HANDLER
    # --------------------------------------------------------

    console_handler = logging.StreamHandler()


    # --------------------------------------------------------
    # FORMATTER
    # --------------------------------------------------------

    formatter = logging.Formatter(
        LOG_FORMAT
    )


    file_handler.setFormatter(
        formatter
    )

    console_handler.setFormatter(
        formatter
    )


    # --------------------------------------------------------
    # ROOT LOGGER
    # --------------------------------------------------------

    root_logger = logging.getLogger()

    root_logger.setLevel(
        log_level
    )


    # --------------------------------------------------------
    # PREVENT DUPLICATE HANDLERS
    # --------------------------------------------------------

    if not root_logger.handlers:

        root_logger.addHandler(
            file_handler
        )

        root_logger.addHandler(
            console_handler
        )