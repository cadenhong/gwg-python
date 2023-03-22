import subprocess, os

'''
This script is modifying the contents of the path environment variable by adding a directory to it.
We then call the myapp command with that modified variable. 
'''

# runs copy() method to the os.environ dictionary that contains the current environment variables
# creates a new dictionary that we can change without modifying the original environment
my_env = os.environ.copy() # Calling this method of the os.environ dictionary will copy the current environment variables to store and prepare a new environment

# using the join() method to append "/opt/myapp/" to the already existing PATH variable
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]]) 

# run the myapp command with the env parameter to the new my_env environment we created
result = subprocess.run(["myapp"], env=my_env)
