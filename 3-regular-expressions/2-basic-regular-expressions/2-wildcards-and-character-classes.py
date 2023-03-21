import re

# Character classes lets us list the characters we want to match inside square brackets
print(re.search(r"[Pp]ython", "Python")) # match either p or P
print(re.search(r"[a-z]way", "The end of the highway")) # any lowercase letter
print(re.search(r"[0-9]th", "The 4th Annual Party")) # any digit
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy")) # match anything defined between [ ]
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9")) # match anything defined between [ ]

# [^] match any character NOT in a group
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")) # returns space
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")) # returns period

# | to match either or of given pattern
print(re.search(r"cat|dog", "I like cats!"))
print(re.search(r"cat|dog", "I like dogs and cats!")) # only matches the first found

# To find all possible matches, use the findall() function
# Returns a list of all matches
print(re.findall(r"cat|dog", "I like dogs and cats and hotdogs!"))

'''
# Check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
'''