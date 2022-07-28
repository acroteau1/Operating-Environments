# 
# This program illustrates how to get the values of 
# 
# 1. The log file
# 2. The document base
# 3. The name of the server
# 

# Import the relevant packages
from configparser import ConfigParser
import configparser
import sys

# Create test class. Declare a parser, and instruct it to write to
# the configuration XML file. Instruct program to output an error
# message in the event of an exception.
class test():
    parser = configparser.ConfigParser()
    try: 
        with open(r"./config.xml", 'w') as cf:
            parser.write(cf)
    except Exception as ce:
        print(str(ce))
        exit()

    # Output the log file, document base, and server name.
    print(parser.getLogFile())
    print(parser.getDocBase())
    print(parser.getServerName())