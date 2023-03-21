import re

# Repeated Matches

# .* matches any character repeated as many times possible (including none):
print(re.search(r"Py.*n", "Pygmalion")) # .* combination extends match range to the whole word
print(re.search(r"Py.*n", "Python Programming")) # matches entire word excluding the last g; GREEDY
print(re.search(r"Py[a-z]*n", "Python Programming")) # Use character class [a-z] to match only Python
print(re.search(r"Py[a-z]*n", "Pyn")) # Also matches no occurrence

# + matches one or more occurences of the character that comes before it:
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly")) # matches `ooll` 
print(re.search(r"o+l+", "boil")) # does not match since there is an `i` between `o` and `l`

# ? matches zero or one occurrence of pattern:
print(re.search(r"p?each", "To each their own")) # p became optional with `?` so it matched `each`
print(re.search(r"p?each", "I like peaches"))

'''
The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice.
For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False.

def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA].*", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
'''