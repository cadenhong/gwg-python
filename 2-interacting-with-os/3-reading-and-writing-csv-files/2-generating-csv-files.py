import csv

hosts = [["workstation.local", "192.168.25.46"], ["workstation.cloud", "10.2.5.6"]]

with open("hosts.csv", "w") as hosts_csv:
  writer = csv.writer(hosts_csv)  # writer variable is an instance of CSV writer class
  writer.writerows(hosts)         # calling writerows() since we know all the data to write