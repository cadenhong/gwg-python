import re

# Matching countries that start with `A` and end with `a`
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan")) # shouldn't match but did since we didn't specify if it should end with `a`
print(re.search(r"^A.*a$", "Azerbaijan")) # correct regex pattern

# Matching valid Python variable names that contain letters, numbers, underscores but cannot start with numbers
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable name"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2nd_variable"))

'''
Check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 

def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
'''