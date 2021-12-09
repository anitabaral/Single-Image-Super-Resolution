import os
import logging
import datetime

from utils.utils import ROOT_DIR
from utils.variables import var

logs_folder = os.path.join(ROOT_DIR, "logs")

if not os.path.exists(logs_folder):
    os.makedirs(logs_folder)

# Create a custom logger
logger = logging.getLogger(__name__)

# Setting global logging level
logger.setLevel(var.log_level)

date = str(datetime.date.today()).replace("-", "")
# Initialize handlers
file_handler = logging.FileHandler(f"{logs_folder}/q_logs_{date}.log")
cli_handler = logging.StreamHandler()
# Set logging level
file_handler.setLevel(level=logging.DEBUG)
cli_handler.setLevel(level=logging.DEBUG)
# Add formatters to handlers
logger_text_format = logging.Formatter(var.log_format)

file_handler.setFormatter(logger_text_format)
cli_handler.setFormatter(logger_text_format)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(cli_handler)
