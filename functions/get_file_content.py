import os
from functions.config import MAX_CHARS


def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory, file_path)
    
    if working_directory not in os.path.abspath(path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            return file_content_string
    except Exception as e:
        return f"Error: {e}"

