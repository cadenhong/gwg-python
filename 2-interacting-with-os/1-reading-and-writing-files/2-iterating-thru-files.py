######### Iterating Through Files #########
with open("spider.txt") as f:
  for line in f:
    print(line.strip().upper()) # strip removes newlines at the end

file = open("spider.txt")
lines = file.readlines()
file.close()
sorted_lines = lines.sort()
print(sorted_lines)