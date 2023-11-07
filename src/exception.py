# Import necessary modules
import sys


# Function to generate a detailed error message
# Parameters:
#   error (str): The error message or description.
#   error_detail (sys): The system information related to the error.
# Returns:
#   str: A detailed error message including file name, line number, and error description.
def error_message_detail(error, error_detail: sys):
    # Get information about the exception
    _, _, exc_tb = error_detail.exc_info()
    # Extract the file name and line number where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    # Create the error message with file name, line number, and error description
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, line_number, str(error))
    return error_message

# Custom Exception class that extends the base Exception class
class CustomException(Exception):
    # Constructor for CustomException
    # Parameters:
    #   error_message (str): The error message or description.
    #   error_detail (sys): The system information related to the error.
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # Generate an error message with detailed information
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # String representation of the CustomException
    def __str__(self):
        return self.error_message
