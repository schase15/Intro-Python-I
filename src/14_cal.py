"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# Fetch command line arguments for this program
'''
sys.argv - returns the arguments that are passed in the terminal.
Always returns the file name, and then user inputs
'''
num_args = len(sys.argv)

# Write a program that prints the monthly calender given the user input from the terminal


  # Set variables for todays date using datetime
today_date = datetime.now()
month = today_date.month
year = today_date.year
cal = calendar.TextCalendar()

  # If the user does not specify any input, print the current month calander
if num_args == 1:
  cal.prmonth(year, month)

  # If the user specifies one argument, print their selected month in the current year
elif num_args == 2:
  user_month = int(sys.argv[1])
  cal.prmonth(year, user_month)

  # If the user specifies two arguments, print their selected month and year calander
elif num_args == 3:
  user_month = int(sys.argv[1])
  user_year = int(sys.argv[2])
  cal.prmonth(user_year, user_month)

  # If they pass in more than two arguments, return an error message specifying that they can pass up to two arguments
else:
  #print a usage statement
  print("Usage: 14_cal.py [month] [year]")

  # Exit the program - pass in 1 to communicate that there was an error (status code)
  # default is 0, usually understood as a success code. We want to clarify that it was not successful
  sys.exit(1)





