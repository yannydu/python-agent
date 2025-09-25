import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
    path = os.path.join(working_directory, directory)

    # Check path is in working dir bounds
    if working_directory not in os.path.abspath(path): 
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory\n'

    # List the contents of dir with their respective sizes and is_dir
    contents = os.listdir(path)
    res = ""
    for content in contents:
        content_path = os.path.join(path, content)
        file_size = os.path.getsize(content_path)        
        is_dir = os.path.isdir(content_path)
        res += f"- {content}: file_size={file_size} bytes, is_dir={is_dir}\n"

    return res

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
