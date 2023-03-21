import re

log = "July 31 07:51:45 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)]" # any one or more occurrences of digits inside square brackets [ ]
result = re.search(regex, log)
print(result[1]) # can get index since we used grouping ()

def extract_pid(log_line):
  regex = r"\[(\d+)]"
  result = re.search(regex, log_line)
  if result is None: # if PID cannot be found
    return "" # return an empty string
  return result[1] # else return the first capturing group

print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]")) # returns an empty string

'''
# Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.

def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

'''