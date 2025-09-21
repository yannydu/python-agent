import os

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
    
