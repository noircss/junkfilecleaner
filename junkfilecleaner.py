import os

def clean_junk_files(folder_path, extensions):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(extensions):
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
            print(f"Removed {file_path}")

# Example usage
folder_path = "/path/to/folder"
extensions = (".tmp", ".bak", ".log") # file extensions to remove
clean_junk_files(folder_path, extensions)
