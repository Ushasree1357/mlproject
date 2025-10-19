import sys
import logging
import os

# ---------- Logging Configuration ----------
LOG_FILE = "app.log"
LOG_PATH = os.path.join(os.getcwd(), LOG_FILE)

# Configure logging to write both to console and file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_PATH),     # logs to file
        logging.StreamHandler(sys.stdout)  # shows logs in console
    ]
)
# -------------------------------------------


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        try:
            a = 1 / 0
        except Exception as e:
            logging.info("Divide by zero")
            raise CustomException(e, sys)
    except CustomException as ce:
        logging.error(ce)  # logs custom error message to both console and file
