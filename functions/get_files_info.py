import os


def get_files_info(working_directory, directory=""):

    full_path = os.path.join(working_directory, directory)

    abs_working = os.path.abspath(working_directory)
    abs_path = os.path.abspath(full_path)

    current = "current" if directory in ("", ".", None) else f"'{directory}'"

    output = f"Result for {current} directory:\n"

    if not os.path.isdir(abs_path):
        output += f'Error: "{abs_working}" is not a directory'
        return output

    if not abs_path.startswith(abs_working):
        output += f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        return output

    output += "Success: \n"
    for file in os.listdir(abs_path):
        if not file.__contains__("pycache"):
            item_path = os.path.join(abs_path, file)
            output += f"- {file}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)} \n"
    return output


print(get_files_info("calculator", "/bin"))
