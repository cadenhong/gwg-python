#!/usr/bin/env python3

import csv
import re

# contains_domain uses regex to identify the domain of the user email addresses in the user_emails.csv file
# It takes address and domain as parameters, and its primary objective is to check whether an email address belongs to the old domain (abc.edu)
def contains_domain(address, domain):
  """Returns True if the email address contains the given domain, in the domain position, false if not."""
  domain_pattern = r"[\w\.-]+@" + domain + "$" # match email addresses of a particular domain
  if re.match(domain_pattern, address):
    return True
  return False

# replace_domain takes in one email address at a time, as well as the email's old domain name and its new domain name
# Primary objective is to replace the email addresses containing the old domain name with new domain name
def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r"" + old_domain + "$" # pattern that identifies sub-strings containing the old domain name within email addresses
  address = re.sub(old_domain_pattern, new_domain, address) # replace the old domain name with the new one
  return address

# Finds the old domain email address, replaces it with the newer one, and writes the updated list to a CSV file in the data directory
def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = "abc.edu", "xyz.edu"
  csv_file_location = "../data/user_emails.csv"
  report_file = "../data/updated_user_emails.csv"

  user_email_list = [] # store user email addresses
  old_domain_email_list = [] # to contain all email addresses with the old domain that regex would match within contains_domain()
  new_domain_email_list = []

  with open(csv_file_location, "r") as f:
    user_data_list = list(csv.reader(f)) # read data from user_emails.csv as a list+
    user_email_list = [data[1].strip() for data in user_data_list[1:]] # add all email addresses into this list

    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address, old_domain, new_domain) # take in the email addresses (with old domain) and replace them with the new domains
        new_domain_email_list.append(replaced_email)

    email_key = ' ' + 'Email Address' # define the headers for our output file through the user_data_list, which contains all the data read from user_emails.csv file
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]: # replace emails within user_data_list by iterating over new_domain_email_list, and replacing the corresponding values in user_data_list
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain

  f.close()

  with open(report_file, "w+") as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()


main()