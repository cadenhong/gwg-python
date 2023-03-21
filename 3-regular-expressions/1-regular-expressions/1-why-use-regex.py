# Simple but error-prone way to search for PID inside square brackets
log = "July 31 07:51:45 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(f"Process ID: {log[index+1:index+6]}")


import re
log = "July 31 07:51:45 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)]"
result = re.search(regex, log)
print(f"Process ID: {result[1]}")
