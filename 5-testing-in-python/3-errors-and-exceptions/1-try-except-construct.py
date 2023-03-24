#!/usr/bin/env python3

def character_frequency(filename):
  """Counts the frequency of each character in a given file"""
  # First try to open the file
  try:
    f = open(filename)
  except OSError: # raised when the OS specific system function returns a system-related or I/O error
    return None
  
  # Now process the file
  characters = {}
  for line in f:
    for char in line:
      characters[char] = characters.get(char, 0) + 1 # see line 22

  f.close()
  return characters

'''
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