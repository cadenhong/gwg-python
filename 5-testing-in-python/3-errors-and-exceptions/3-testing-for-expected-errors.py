#!/usr/bin/env python3

import unittest

def validate_user(username, minlen):
  assert type(username) == str, "username must be a string" # Assert keyword verifies if a conditional expression is true; if false, raises AssertionError (produce a message when a conditional is false)
  
  if minlen < 1:
    raise ValueError("minlen must be at least 1") # ValueError indicates that there's a problem with values of parameters
  
  if len(username) < minlen:
    return False
  
  if not username.isalnum():
    return False
  
  return True

class TestValidateUser(unittest.TestCase):
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)

  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)

  def test_invalid_minlen(self): # assertRaises method from unittest module
    self.assertRaises(ValueError, validate_user, "user", -1) # parameters: (error expected to be raised, function name, parameter to be passed to function, )

unittest.main()