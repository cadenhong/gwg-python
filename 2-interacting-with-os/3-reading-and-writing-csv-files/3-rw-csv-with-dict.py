import csv

with open("software.csv") as software:
  reader = csv.DictReader(software) # DictReader turns each row of a CSV file into a dictionary
  for row in reader:
    print(f"{row['name']} has {row['users']} users")

print("---------------------------------------------")

users = [
  {"name": "Sol Mansi",
   "username": "solm",
   "department": "IT Infrastructure"},
  {"name": "Lio Nelson",
   "username": "lion",
   "department": "UX Research"},
  {"name": "Charlie Grey",
   "username": "greyc",
   "department": "Development"} 
]   # list of dictionary

keys = ["name", "username", "department"]   # a list of column header to be used

with open("write_csv.csv", "w") as file:
  writer = csv.DictWriter(file, fieldnames=keys)  # DictWriter object and fieldnames parameter, which requires a list of keys to indicate header row
  writer.writeheader()  # Writes the header based on the passed fieldnames variable
  writer.writerows(users) # Writes the matching value based on the passed keys
