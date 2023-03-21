import re

result1 = re.search(r"aza", "plaza") # r"" indicates that it's a rawstring; tells python to not interpret any special characters
result2 = re.search(r"aza", "bazaar")
result3 = re.search(r"aza", "maze")
print(result3)

print(re.search(r"^x", "xenon"))
print(re.search(r"ly$", "smartly"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) # pass the IGNORECASE function to ignore case sensitivity

'''
# Check if the text passed contains a, e and i, with exactly one occurrence of any other character in between
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True
'''