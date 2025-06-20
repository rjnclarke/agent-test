import os
import json
from typing import Set, Callable, Any

def large_file_pipeline(file_path: str)-> str:
    """
    Process the file if the it is over 10 megabytes.

    :param file path: The path of the file
    :return: Report that large file pipeline used
    """

    message_json = json.dumps({"message": "The file is processed by the large file pipeline"})
    return message_json
    
def small_file_pipeline(file_path: str)-> str:
    """
    Process the file if the it is over 10 megabytes.

    :param file path: The path of the file
    :return: Report that large file pipeline used
    """

    message_json = json.dumps({"message": "The file is processed by the small file pipeline"})
    return message_json


# Define a set of callable functions
user_functions: Set[Callable[..., Any]] = {
     large_file_pipeline, 
     small_file_pipeline
 }