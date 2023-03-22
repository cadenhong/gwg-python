#!/usr/bin/env python3

import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue

    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    print(result[1])

######################################################################

'''
# Testing REGEX before adding to code

pattern = r"USER \((\w+)\)$" # capturing one or more occurrences of alphanumeric characters inside parentheses after the word USER, found at the end of line
line = "Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1]) # prints `naughty_user`
'''

###################################################################### 

'''
# Same syslog but displaying date, time, and process id inside the square brackets
# We can read each line of the syslog and pass the contents to the show_time_of_pid function
# Extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440

def show_time_of_pid(line):
  pattern = r"^(\w{3}\s{1}\d{1}\s{1}\d{2}:\d{2}:\d{2})\s\w.*([\d]{5,})"
  result = re.search(pattern, line)
  return "{} pid:{}".format(result[1], result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
'''