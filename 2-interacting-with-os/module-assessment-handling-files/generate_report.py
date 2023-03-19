#!/usr/bin/env python3

import csv

# Receives a CSV file and returns a list of dictionaries
def read_employees(csv_file_location):
  # Dialect groups all the parameters to control how CSV parses or writes data;
  # Instead of passing each parameter to reader and writer separately, using a dialect makes it mor$
  ### Registering a dialect empDialect
  ### This dialect removes any leading spaces while parsing the CSV file
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

  # csv.DictReader(file, fieldnames) -> fieldnames parameter should be provided if the first row is$
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')

  # Iterate over the CSV file opened and produce a dictionary from key to values, append to the emp$
  employee_list = []
  for data in employee_file:
    employee_list.append(data)

  return employee_list

employee_list = read_employees('data/employees.csv')
#print(employee_list)

#============================================================================================================

# Should receive the list of dictionaries (i.e. employee_list) and return a dictionary (i.e. depart$
def process_data(employee_list):
  # Iterate over employee_list to add only the department values to department_list
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])

  # Remove redundancy using set() and return a dictionary in the format of department:amount
  # where amount is the number of employees in that particular department
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)

  return department_data

dictionary = process_data(employee_list)
#print(dictionary)

#============================================================================================================

# Writes a dictionary of department:amount to a file in the following format:
# <department1>:<amount1>
# <department2>:<amount2>
def write_report(dictionary, report_file):
  # Open report_file in w+ mode to enable both reading and writing/overwriting
  # Iterate through the dictionary and use write() to store data
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k) + ':' + str(dictionary[k]) + '\n')
    f.close()

write_report(dictionary, 'data/test_report.txt')
