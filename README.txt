##############################################################################
this is a simple implemantation of routines that move a times series from any local time to UTC.
the code read a text file separete the columns parse the column with date time, 
moves the time zone from the required one to Universal Time and wirtes a second file with asame name plus "_ToUTC"
that in the first line indicates the time zone of origin.  
the code can be used as a test see datetime_test.py
or using a simple interface in made for PyQt4 upgraded at PyQt5
##############################################################################
for time zone names use:
--------------------------------
 for tz in pytz.all_timezones:
    print tz
--------------------------------
or search on the web:
https://exceptionshub.com/python-pytz-list-of-timezones.html
##############################################################################