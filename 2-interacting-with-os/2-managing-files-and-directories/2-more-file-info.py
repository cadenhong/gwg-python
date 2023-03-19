### More file information ###
import os
import datetime

size = os.path.getsize("first_draft.txt") # check file size in bytes
last_modified = os.path.getmtime("first_draft.txt") # check when file was last modified
print(size)
print(last_modified) # unix timestamp
print(datetime.datetime.fromtimestamp(last_modified)) # convert to readable timestamp
print(os.path.abspath("first_draft.txt")) # absolute path of file