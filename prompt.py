## A prompt.py file is a file creates a prompt for ChatGPT of the codebase to make it easy.

import os

def get_code_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

# Get the current directory
current_dir = os.getcwd()

# Get the list of files in the current directory
files = os.listdir(current_dir)

# Loop through the files and save the code to a text file, separated by dashes, and the file name
with open('code.txt', 'w') as f:
    for file in files:
        if file.endswith('.py'):
            code = get_code_from_file(file)
            f.write('-' * 80 + ' ' + file + ' ' + '-' * 80 + ' ' + ' ' + code + ' ' + ' ') #add a space at the end to make sure the next file starts on a new line