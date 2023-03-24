import re 
  
my_txt = "An investment in knowledge pays the best interest."

# finds all matches for the letters a through c in an input string if followed by another 
# character and returns them as a list of strings, with each string representing one match
def LetterCompiler(txt):
  result = re.findall(r'([a-c]).', txt)
  if result is None:
    return txt
  return result

print(LetterCompiler(my_txt))

######

import unittest

class TestCompiler(unittest.TestCase):
  def test_basic(self):
    testcase = "The best preparation for tomorrow is doing your best today."
    expected = ['b', 'a', 'a', 'b', 'a']
    self.assertEqual(LetterCompiler(testcase), expected)

class TestCompiler2(unittest.TestCase):
  def test_two(self):
    testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
    expected = ['b', 'c']
    self.assertEqual(LetterCompiler(testcase), expected)

class TestCompiler3(unittest.TestCase):
  def test_two(self):
    testcase = ""
    expected = []
    self.assertEqual(LetterCompiler(testcase), expected)

unittest.main()