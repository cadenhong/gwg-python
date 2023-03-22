#!/usr/bin/env python3

import sys
import os
import re

'''
Search for the CRON error that failed to start by narrowing the search to "CRON ERROR Failed to start"
'''
def error_search(log_file):
  error = input("What is the error? ") # ask user to define type of error to search
  returned_errors = [] # list of returned errors

  with open(log_file, mode="r", encoding="UTF-8") as file: # open log file and use 'UTF-8' encoding
    for log in file.readlines(): # read each log separately using readlines()
      error_patterns = ["error"] # initial pattern to filter all ERROR logs only; can change to INFO or WARN

      for i in range(len(error.split(' '))): # add whole user input to error_patterns list
        error_patterns.append(r"{}".format(error.split(' ')[i].lower())) # error_patterns = ["cron", "error", "failed", "to", "start"]

      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns): # all() returns True if all items in an iterable are true, otherwise it returns False
        returned_errors.append(log) # check whether log line has user defined pattern and if present, append to returned_errors list

    file.close()

  return returned_errors

'''
Create an output file that has all returned_errors
'''
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/4-managing-data-and-processes/module-assessment-managing-data-and-processes/data/errors_found.log', 'w') as file: # os.path.expanduser ('~') returns the home directory of your system instance and concatenate to the errors_found.log
    for error in returned_errors:
      file.write(error) # write all returned_errors into the errors_found.log file
    
    file.close()


'''
Main function that calls both error_search() and file_output()
- log_file takes in the path of the log file passed in as a parameter (i.e. fishy.log)
- error_search() takes in the log_file as parameter and returns a list of errors to be stored in returned_errors
- file_output() takes in the returned_errors as parameter and creates a file
- sys.exit(0) means a successful termination; nonzero is an abnormal termination
'''
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)