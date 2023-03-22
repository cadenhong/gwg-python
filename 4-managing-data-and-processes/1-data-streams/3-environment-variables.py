# Using Python to read environment variables

import os

# using environ dictionary and using the get() method to access dictionary values
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", "")) # empty string returned if key not found
print("FRUIT: " + os.environ.get("FRUIT", "this string since it wasn't found")) # empty string returned if key not found