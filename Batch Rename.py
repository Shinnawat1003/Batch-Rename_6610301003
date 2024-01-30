import os

def rename_files(directory, file_type):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    filtered_files = [f for f in files if f.endswith(file_type)]
    filtered_files.sort()

    for index, filename in enumerate(filtered_files, start=1):
        new_filename = f"{index:03d}{file_type}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed file '{filename}' to '{new_filename}'")

# Example usage
directory_path = "D:\Mr.G\p1"
file_extension = "jpg"
rename_files(directory_path, file_extension)
