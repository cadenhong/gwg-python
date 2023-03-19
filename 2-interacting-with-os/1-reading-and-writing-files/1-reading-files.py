######### Reading Files #########
file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

with open("spider.txt") as f: # closes automatically
  print(f.readline())