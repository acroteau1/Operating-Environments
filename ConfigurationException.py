# 
# ConfigurationException.py
# 
# @author Alison Croteau
# Original Java file by Gagne, Galvin, Silberschatz
# Operating System Concepts with Java - Eighth Edition
# Copyright John Wiley & Sons - 2010
# 

# Create ConfigurationException class extending Exception class
# the super() function allows us to call methods of the base class
# via delegation, allowing us to use different base classes at 
# different times.
exception = ""
class ConfigurationException(Exception):
        def __init__(self, message):
            super(MyException, self).__init__(message)
            self.message = message