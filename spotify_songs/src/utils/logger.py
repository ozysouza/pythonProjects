import logging


def setup_logging(log_file='app.log'):
    # Create a logger object
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the default logging level

    # Create a console handler with a specific format
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('\n%(levelname)s %(asctime)s - %(message)s', datefmt='%H:%M:%S')
    console_handler.setFormatter(console_format)

    # Create a file handler with a specific format
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')
    file_handler.setFormatter(file_format)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def show_logging(message, level=logging.INFO):
    logger = logging.getLogger()

    if level == logging.DEBUG:
        logger.debug(message)
    elif level == logging.INFO:
        logger.info(message)
    elif level == logging.WARNING:
        logger.warning(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.CRITICAL:
        logger.critical(message)
    else:
        logger.info(message)