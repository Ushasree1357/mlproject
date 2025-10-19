import logging
import os
from datetime import datetime

# Create a logs directory if it doesn’t exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create a timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure the main logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Add a console handler to also print logs in the terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(levelname)s - %(message)s"))
logging.getLogger().addHandler(console_handler)
