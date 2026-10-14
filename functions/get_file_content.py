import os
from config import MAX_CHARS_TO_READ_FROM_FILE

debug_var = False

def output_handle (output):
    if debug_var:
        print(output)

    return output


def get_file_content(working_directory: str, file_path: str) -> str:
    full_path = os.path.join(working_directory, file_path)

    abs_working = os.path.abspath(working_directory)
    abs_path = os.path.abspath(full_path)

    current = "current" if file_path in ("", ".", None) else f"'{file_path}'"

    output = f"Result for {current}:\n"

    if not os.path.isfile(abs_path):
        output += f'Error: File not found or is not a regular file: "{file_path}"'
        return output_handle(output)

    if not abs_path.startswith(abs_working):
        output += f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        return output_handle(output)

    output += "Success: \n"
    with open(abs_path, "r") as f:
        output += f.read(MAX_CHARS_TO_READ_FROM_FILE)
        # After reading the first MAX_CHARS...
        #
        if f.read(1):
            output += f'[...File "{file_path}" truncated at {MAX_CHARS_TO_READ_FROM_FILE} characters]'

    return output_handle(output)

schema_get_files_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Lists reads file content in a specified directory relative to the working directory, reading only up to the max chars in the config file.",
        "parameters": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "File path to read from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
