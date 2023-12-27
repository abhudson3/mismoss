import os
import shutil
import subprocess
import json
def move_js_files_to_top(root_dir):
    # Loop through all items in the root directory
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        # Check if the item is a directory
        if os.path.isdir(path):
            # Walk through the directory
            for subdir, dirs, files in os.walk(path):
                for file in files:
                    # Check if the file is a JavaScript file
                    if file.endswith('.js'):
                        source_file_path = os.path.join(subdir, file)
                        destination_file_path = os.path.join(path, file)
                        # Move the JavaScript file to the top of the directory
                        shutil.move(source_file_path, destination_file_path)
                        print(f"Moved: {source_file_path} to {destination_file_path}")

# Replace 'path_to_student_folders' with the path to the directory containing student folders
# print("What is the directory you would like to point the run moss on?")
root_directory = 'moss'
move_js_files_to_top(root_directory)