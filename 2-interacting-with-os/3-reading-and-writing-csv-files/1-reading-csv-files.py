import csv

with open("csv_file.txt") as file:
  csv_f = csv.reader(file)    # reading file as a csv object called csv_f
  for row in csv_f:
    name, phone, role = row   # unpacking each column of row to variables name, phone, and role
    print(f"Name: {name}, Phone: {phone}, Role: {role}")
