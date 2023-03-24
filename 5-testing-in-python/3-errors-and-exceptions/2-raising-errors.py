#!/usr/bin/env python3

def validate_user(username, minlen):
  assert type(username) == str, "username must be a string" # Assert keyword verifies if a conditional expression is true; if false, raises AssertionError (produce a message when a conditional is false)
  
  if minlen < 1:
    raise ValueError("minlen must be at least 1") # ValueError indicates that there's a problem with values of parameters
  
  if len(username) < minlen:
    return False
  
  if not username.isalnum():
    return False
  
  return True

print(validate_user("hello", 2))
print(validate_user("invalid", -2)) # ValueError: minlen must be at least 1
print(validate_user(88, 2)) # AssertionError: username must be a string
print(validate_user(["anothername"], 4)) # AssertionError: username must be a string