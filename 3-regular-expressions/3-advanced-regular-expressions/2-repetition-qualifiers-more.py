import re

# Numeric repetition qualifiers specifies a range -> {}
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) # returns ['scary', 'ghost', 'appea']

# \b matches word limits at the beginning and end of the pattern; find full words that are exactly the range
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")) # returns ['scary', 'ghost']

print(re.findall(r"\w{5,10}", "I really like strawberries")) # matches words between 5-10 characters, returns ['really', 'strawberri']
print(re.findall(r"\w{5,}", "I really like strawberries")) # matches words that are 5+ characters, returns ['really', 'strawberries']
print(re.search(r"s\w{,20}", "I really like strawberries")) # match word that starts with an s followed by upto 20 alphanumeric characters

'''
Returns all words that are at least 7 characters:

def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []
'''