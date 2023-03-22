#!/usr/bin/env python3

import sys

# command line arguments are stored in the sys module

print(sys.argv) # shows a list of command line arguments passed


# Exit Status > value returned by program from shell
# echo $?  # prints the exit status


'''
The script below recieves a file name as the command line argument.
First checks if the file name exists or not.
If it doens't exist, it creates it by writing a line to it.
Otherwise, it prints an error message and exists with exit value 1.
'''
import os, sys

filename = sys.argv[1]

if not os.path.exists(filename):
  with open(filename, "w") as f:
    f.write("New file created\n")
else:
  print("Error, the file {} already exists!".format(filename))
  sys.exit(1)

# Run `echo $?` after running the script to see the error code