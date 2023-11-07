# Import necessary modules for logging and file operations
import logging
import os
from datetime import datetime

# Define a constant variable for the log file name, using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a path to store log files in the 'logs' directory, ensuring it exists
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# Create a full path to the log file by joining the logs_path and LOG_FILE
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging module with desired settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path for saving log entries
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define log message format
    level=logging.INFO,  # Set the log level to INFO, so it logs messages at INFO level and above
)
