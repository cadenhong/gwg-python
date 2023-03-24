#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

# Creating our own TestRearrange class that inherits from unittest.TestCase class
# unittest.TestCase class comes with a bunch of testing methods
class TestRearrange(unittest.TestCase): # Include the class we wantn to inherit inside the parenthesis

  # Basic case
  def test_basic(self): # Any methods that start with `test` will automatically become tests that can be run by the framework
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

  # Edge case
  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase),expected)

  def test_double_name(self):
    testcase = "Hopper, Grace M."
    expected = "Grace M. Hopper"
    self.assertEqual(rearrange_name(testcase),expected)

  def test_one_name(self):
    testcase = "Voltaire"
    expected = "Voltaire"
    self.assertEqual(rearrange_name(testcase),expected)

unittest.main() # Running the test