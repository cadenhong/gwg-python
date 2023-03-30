#!/usr/bin/env python3

import sys
import subprocess

# must pass oldFiles.txt as a parameter - stored inside sys.argv[1]
with open(sys.argv[1], "r") as f:
  content = f.readlines()

  for line in content:
    old = str(line.split()[0])
    new = old.replace("jane", "jdoe")
    subprocess.run(["mv", old, new])

'''
Takes oldFiles.txt as a command line argument and then renames files with the new username "jdoe"
'''