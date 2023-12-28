import mosspy
import subprocess
import re
import os
import shutil
import json
import stat

#   YOU WILL NEED TO RUN "pip install mosspy" FOR THIS TO WORK 
#   you will not be able to run pip without python btw

def extract_substring_after_moss(input_string):
    pattern = r"mis.*?submissions"
    match = re.search(pattern, input_string)
    if match:
        return match.group()
    else:
        return "No match found for the pattern"


def move_js_files_to_top(root_dir, language):
    # Loop through all items in the root directory
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        # Check if the item is a directory
        if os.path.isdir(path):
            # Walk through the directory
            for subdir, dirs, files in os.walk(path):
                for file in files:
                    # Check if the file is a JavaScript file
                    if file.endswith(language):
                        source_file_path = os.path.join(subdir, file)
                        destination_file_path = os.path.join(path, file)
                        # Move the JavaScript file to the top of the directory
                        shutil.move(source_file_path, destination_file_path)
                        print(f"Moved: {source_file_path} to {destination_file_path}")




def clone_repos(assnCode, directory):
    """List repositories of a given GitHub assignment code."""
    command = ["gh", "classroom", "clone", "student-repos", "-a", assnCode, "--directory", directory, "--all"]


    # runs the above repo clone command, which returns the output of the command
    unfilteredOutputDir = run_cli_command(command, "submission")
    # filters the command output to get the name of the directory that the repos were cloned into
    outputDir = extract_substring_after_moss(unfilteredOutputDir)
    # returns the directory that the repos were cloned into
    return outputDir

def run_cli_command(command, keyword):
    """Run a command and return the output."""
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(f"Error running command: {result.stderr}")
    captured_output = process_output(result.stdout, keyword)
    return captured_output

def process_output(output, keyword):
    """Process the output to extract the desired information."""
    # Placeholder for how you might process the output
    # For example, capturing lines that contain a specific keyword
    for line in output.split('\n'):
        if keyword in line:
            return line  # or accumulate in a list if multiple lines are expected
    return "No relevant information found"  # Placeholder response



def main():
    try:
        userid = 813921095
        assnCode = input("\nMISMoss - 2023 \n \nWhat is the assignment code of the assignment you would like to check?\n\n(you can find this by going to gh classroom, clicking an assignment, clicking download,\n selecting student repositories, and copying the numbers at the end of the command in the box)\n")
        directory = input("\nWhat is the directory you would like to run the program in? \nIf one does not exist by the name provided, one will be created.\n")
        language = input("\nPlease type in the file extension for the language you would like to check in the following format: .js\n")
        fullLanguage = ""
        if(language == ".js"):
            fullLanguage = "javascript"
        elif(language == ".cs"):
            fullLanguage = "csharp"

        m = mosspy.Moss(userid, fullLanguage)


        while True:
            add_more = input("\nDo you want to add a base file? (yes/no): \n").strip().lower()

            if add_more in ["yes", "y"]:
                # User wants to add a base file, ask for the file path
                file_path = input("\nEnter the path to the base file or the name of the file: \n").strip()
                try:
                    m.addBaseFile(file_path)
                    print(f"Base file '{file_path}' added.")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                break
               


        print("cloning repos...")
                
        # output directory is equal to the name of the directory all of the repos were cloned into
        outputDir = clone_repos(assnCode, directory)
        move_js_files_to_top("./" + directory + "/" + outputDir, language)

        # Submission Files
        m.setDirectoryMode(1)
        m.addFilesByWildcard("./" + directory + "/" + outputDir + "/*/*" + language)

  
        url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
        print()

        print ("Report Url: " + url)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
