import re

# split() takes any regular expression as a separator
print(re.split(r"[.?!]", "One sentence. Another one? And last one!")) # returns without the pattern: ['One sentence', ' Another one', ' And last one', '']
print(re.split(r"([.?!])", "One sentence. Another one? And last one!")) # returns both sentence and punctuation: ['One sentence', '.', ' Another one', '?', ' And last one', '!', '']

# sub() is used for creating new strings by substituting all or part of them for a different string
# similar to replace but using regex for matching and replacing
print(re.sub("[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts85@my.example.com"))
  # part before the @ sign: include alphanumeric characters . $ + -
  # part after the @ sign: only include alphanumeric characters . -

# using sub to produce a replaced string
print(re.sub(r"^([\w \.-]*), ([\w \.-]*)$", r"\2 \1", "Lovelace, Ada")) # pattern, \2 to indicate second captured group and \1 to indicate first caputured group, and input

'''
# Split a piece of text by either the word "a" or "the":

re.split(r"the|a", "One sentence. Another one? And the last one!") # returns ['One sentence. Ano', 'r one? And ', ' l', 'st one!']
'''