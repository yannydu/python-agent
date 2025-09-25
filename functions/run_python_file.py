import os
import subprocess
from google import genai
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):

    working_abspath = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    if working_abspath not in target_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(["python3", target_path] + args, timeout=30, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        error_msg = ""
        if completed_process.returncode != 0:
            error_msg = f"Process exited with code {completed_process.returncode}"

        if not completed_process.stdout and not completed_process.stderr:
            return "No output produced."

        return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\n{error_msg}"

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=f"Executes the specified python file in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path where the file exists, relative to where the working directory is.",
            )
        }
    )
)
