import os

def write_file(working_directory: str, file_path: str, content: str) -> str:

    full_path = os.path.join(working_directory, file_path)

    abs_working = os.path.abspath(working_directory)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(abs_working):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(abs_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, "w") as f:
        f.write(content)
        f.close()


    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
