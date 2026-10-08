import os
import subprocess
from sys import stderr, stdin

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    timeout = 30

    full_path = os.path.join(working_directory, file_path)

    abs_working = os.path.abspath(working_directory)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(abs_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", abs_path]
    if args is not None:
        command.extend(args)
    def open_file ():
        try:
            result = subprocess.run(command, cwd=abs_working, capture_output=True, text=True, timeout=timeout, check=False)
            if result.returncode != 0:
                return f"Process exited with code {result.returncode}"

            if result.stderr == "" and result.stdout == "":
                output = "No output produced"

            else:
                output = f"STDOUT: {result.stdout} \n STDERR: {result.stderr}"
            return output
        except Exception as e:
            return f"Error: executing Python file: {e}"

    output = open_file()


    return output
