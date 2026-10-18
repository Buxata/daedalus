import os
from config import DEBUG_VAR

debug_var = DEBUG_VAR

def output_handle (output):
    if debug_var:
        print(output)
    return output

def get_files_info(working_directory, directory=""):

    full_path = os.path.join(working_directory, directory)

    abs_working = os.path.abspath(working_directory)
    abs_path = os.path.abspath(full_path)

    current = "current" if directory in ("", ".", None) else f"'{directory}'"

    output = f"Result for {current} directory:\n"

    if not os.path.isdir(abs_path):
        output += f'Error: "{abs_working}" is not a directory'
        return output_handle(output)

    if not abs_path.startswith(abs_working):
        output += f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        return output_handle(output)

    output += "Success: \n"
    for file in os.listdir(abs_path):
        if not file.__contains__("pycache"):
            item_path = os.path.join(abs_path, file)
            output += f"- {file}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)} \n"
    return output_handle(output)

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
