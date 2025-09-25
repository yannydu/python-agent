import os
from functions.config import MAX_CHARS
from google import genai
from google.genai import types


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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Lists up to {MAX_CHARS} characters of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file that was read, relative path to the working directory.",
            )
        }
    )
)
