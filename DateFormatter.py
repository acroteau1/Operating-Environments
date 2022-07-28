# 
# DateFormatter.py
# 
# @author Alison Croteau
# Original Java file by Gagne, Galvin, Silberschatz
# Operating System Concepts with Java - Eighth Edition
# Copyright John Wiley & Sons - 2010
# 

# Import relevant classes
from datetime import date
from datetime import datetime
from datetime import time

# Create DateFormatter class. Create a variable for current date and time. Modify
# the rightNow variable into the datetime format created in the original files. Declare
# output string and set it to the SimpleDateFormat variable.
class DateFormatter():
    rightNow = datetime.now()
    SimpleDateFormat = rightNow.strftime("%d-%b-%Y %H:%M:%S")
    output = ""

    output = SimpleDateFormat
    # Print the current date and time in the specified format.
    print(output)