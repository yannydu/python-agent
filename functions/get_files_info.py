import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory\n'

    try:    
        # List the contents of dir with their respective sizes and is_dir
        files_info = []
        for content in os.listdir(target_dir):
            content_path = os.path.join(target_dir, content)
            file_size = os.path.getsize(content_path)        
            is_dir = os.path.isdir(content_path)
            files_info.append(
                f"- {content}: file_size={file_size} bytes, is_dir={is_dir}\n"
            )
        return files_info
    except Exception as e:
        return f"Error listing files: {e}"


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
