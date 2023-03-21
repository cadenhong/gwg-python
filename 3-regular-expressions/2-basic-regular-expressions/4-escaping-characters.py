import re

# To match one of the special characters learned .*+?^$[], use escape characters

# \ to escape special characters
print(re.search(r".com", "welcome")) # prints that there's a match when we wanted `.com`
print(re.search(r"\.com", "welcome")) # escaping the dot removes the match
print(re.search(r"\.com", "example.com")) # matches the actual pattern we are looking for

# \w matches letters, numbers, underscores (alphanumeric characters)
print(re.search(r"\w*", "This is an example")) # matched `this` since space is not included in \w
print(re.search(r"\w*", "And_This_Is_Another"))

# \d for digits
# \s for whitespace characters (space, tab, newline)
# \b for word boundaries

'''
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.

def check_character_groups(text):
  result = re.search(r"\w\s", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
'''