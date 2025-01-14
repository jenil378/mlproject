import sys
from src.logger import logging  # Import the logger configuration

# Function to get detailed error message
def error_message_detail(error, error_detail: sys):
    # Extract details about the exception
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Initialize the parent Exception class
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

        # Log the error message
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message

# Example usage
if __name__ == "__main__":
    try:
        # Intentional division by zero to raise an exception
        result = 1 / 0
    except Exception as e:
        # Raise the custom exception
        raise CustomException("A division by zero occurred", sys)
