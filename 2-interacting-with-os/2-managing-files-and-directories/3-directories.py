import os

print(os.getcwd()) # current working directory
#os.mkdir("newer_dir/even_newer") # make new directory
#print(os.listdir("newer_dir")) # list directory content

dir = "newer_dir"
for name in os.listdir(dir):
  fullname = os.path.join(dir, name) # create full path to use isdir(), NOT OS SPECIFIC!!!
  if os.path.isdir(fullname): # checks if item is a directory
    print(f"{fullname} is a directory")
  else:
     print(f"{fullname} is a file")


os.rmdir("new_dir") # remove directory)