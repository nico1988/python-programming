import logging

def setup_logging():
    """
    Set up logging configuration.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    return logger

setup_logging()

# Example usage
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.info("Logging setup complete.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.debug("This is a debug message.")
    logger.critical("This is a critical message.")