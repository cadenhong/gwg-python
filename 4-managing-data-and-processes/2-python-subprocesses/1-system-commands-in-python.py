# Executing system commands using subprocess module
'''
The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
https://docs.python.org/3/library/subprocess.html
'''

# This script is considered a parent process

import subprocess

subprocess.run(["date"]) # child process where the command is executed

subprocess.run(["sleep", "2"])

result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode) # returns the error code 1 of the completed process

# subprocess run outputs will print to the screen