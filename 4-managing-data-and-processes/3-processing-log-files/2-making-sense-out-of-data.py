#!/usr/bin/env python3

import sys
import re

'''
usernames = {}
name = "good_user"

# taking the current value in the dictionary and passing a default value of 0 so we get the default value if it doesn't exist
# then add one and set it as a new value associated with the key
usernames[name] = usernames.get(name, 0) + 1
print(usernames) # returns {'good_user': 1}

###################################
# dictionary.get(keyname, value) 
# keyname 	Required   The keyname of the item you want to return the value from
# value    	Optional   A value to return if the specified key does not exist; default is None

# Example:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)
y = car.get("brand", "VW")

print(x) # returns 15000
print(y) # returns "Ford"
###################################
'''

logfile = sys.argv[1]
usernames = {}

with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue # skip this iteration

    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    
    if result is None:
      continue # skip this iteration

    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1

print(usernames)

# running this file: ./2-making-sense-out-of-data.py syslog
# returns: {'good_user': 1, 'naughty_user': 3}