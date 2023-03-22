# Capturing output from a command and using it for something else in a script

import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True) # capture_output=True allows us to store the output of a system command
print(result.returncode) # 0

# b in front of the result indicates that this is not a proper string, but an array of bytes
print(result.stdout) # b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'

# decode() applies UTF-8 encoding to transform bytes into a string
# split() turns it into a list
print(result.stdout.decode().split()) # ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

######################################################################

# Looking at stderr
another_result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(another_result.returncode) # 1
print(another_result.stdout) # b''
print(another_result.stderr) # b'rm: does_not_exist: No such file or directory\n'