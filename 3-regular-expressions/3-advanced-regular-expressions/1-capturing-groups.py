# Capturing groups - portions of pattern that are enclosed in parentheses

import re

result = re.search(r"^(\w*), (\w*)$", "Bond, James")
print(result)

# groups() function to see the groups captured
print(result.groups()) # since we defined two groups in the search using (), this returns a tuple of two elements
print(result[0]) # first index always stores the text matched by the entire regex
print(result[1]) # returns "Bond"
print(result[2]) # returns "James"
print(f"{result[2]} {result[1]}") # returns James Bond

# function to return rearranged name
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name)
  if result is None:
    return name
  return f"{result[2]} {result[1]}"

rearrange_name("Bond, James")
rearrange_name("Doe, Jane")
rearrange_name("Grimm, Eli")
rearrange_name("Hopper, Grace M.") # does not work since it has space and .

# revised function to account for middle initials
def rearrange_name_revised(name):
  result = re.search(r"^([\w]*), ([\w* \.])$", name)
#  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name) # << correct answer
  if result is None:
    return name
  return f"{result[2]} {result[1]}"

print(rearrange_name_revised("Hopper, Grace M."))
print(rearrange_name_revised("Kennedy, John F."))