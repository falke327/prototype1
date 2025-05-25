import logging
import os
from datetime import datetime

def setup_logger(name: str, is_pi: bool) -> logging.Logger:
    # choose log directory
    if is_pi:
        log_dir = '/var/log/falk'
    else:
        log_dir = os.getcwd()

    os.makedirs(log_dir, exist_ok=True)

    # filename
    today = datetime.now().strftime("%d-%m-%Y")
    log_file = os.path.join(log_dir, f"falk-{today}.log")

    # logger config
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s - [%(levelname)s] - %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
