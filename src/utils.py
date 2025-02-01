import logging

def setup_logging():
    """Configure logging settings."""
    logging.basicConfig(
        level=logging.INFO,
        filename="logs/bot.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
