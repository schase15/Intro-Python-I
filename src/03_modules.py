"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("There is only one argument. It is: " , str(sys.argv))
print("___________________")

# Print out the OS platform you're using:
print("The name of the platform I am using is: ", sys.platform)
print("___________________")

# Print out the version of Python you're using:
print("The version of Python I am using is: ", sys.version)
print("___________________")


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current process ID: ", os.getpid())
print("___________________")

# Print the current working directory (cwd):
print("Current working directory: ", os.getcwd())
print("___________________")

# Print out your machine's login name
print("Machine's login name: ", os.getlogin())
print("___________________")
