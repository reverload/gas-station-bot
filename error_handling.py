# error_handling.py

import logging

# Initialize logger for error handling
logger = logging.getLogger(__name__)

def handle_api_error(error_message):
    """
    Handles errors related to API requests.

    Parameters:
    - error_message: A string containing the error message to be logged.
    """
    # Log the error message
    logger.error(f"API Error: {error_message}")

def handle_data_processing_error(error_message):
    """
    Handles errors related to data processing.

    Parameters:
    - error_message: A string containing the error message to be logged.
    """
    # Log the error message
    logger.error(f"Data Processing Error: {error_message}")

def handle_general_error(error_message):
    """
    Handles general errors that may occur during the bot's operation.

    Parameters:
    - error_message: A string containing the error message to be logged.
    """
    # Log the error message
    logger.error(f"General Error: {error_message}")
