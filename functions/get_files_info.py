import os

def get_files_info(working_directory, directory=""):
    full_path = os.path.join(working_directory, directory)

    if not full_path.startswith(working_directory):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.isdir(full_path):
        print(f'Error: "{directory}" is not a directory')

    for file in os.listdir(full_path):
        item_path = os.path.join(full_path,file)
        info = os.stat(item_path)
        print(f'- {file}: {os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)} ')
        
    
get_files_info("calculator",".")