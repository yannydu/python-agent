import os
from google import genai
from google.genai import types

def write_file(working_directory, file_path, content):
    working_abspath = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    if working_abspath not in target_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
    if not os.path.isfile(target_path):
        try:
            open(target_path, "x")
        except Exception as e:
            return f"Error: {e}"

    try:
        with open(target_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Writes to the specified file in the working directory, creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents written to the file.",
            )
        }
    )
)
