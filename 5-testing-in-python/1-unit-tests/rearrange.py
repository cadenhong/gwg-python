import re

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)

  # Handling an edge case by checking the result variable before operating with it
  if result is None: # empty string and single name covered under this condition
    return name
  
  return "{} {}".format(result[2], result[1])