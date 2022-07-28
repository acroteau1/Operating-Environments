# 
# HTTPHeader.py
# This program returns the header output from a web server.
# 
# Usage: python HttpHeader <web server> [document name]
# 
# @author Alison Croteau
# Original Java file by Gagne, Galvin, Silberschatz
# Operating System Concepts with Java - Eighth Edition
# Copyright John Wiley & Sons - 2010
# 

# Import the relevant packages
import sys
import io
import socket

# Create HttpHeader class. Define an I/O exception based on lack of arguments
# and format the system to output a specific error for this event.
class HttpHeader():
    def IO_exception(*args):
        result = args[0]
        for x in args:
            if x < 1:
                sys.stderr.write("Usage: python HttpHeader <web server> [document name]")
                break
        # Declare a few variables, including blank string requestedDocument, local host,
        # a socket, and port to listen on. 
        requestedDocument = ""
        HOST = "127.0.0.1"
        PORT = 80
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if x == 2:
            requestedDocument = args[1]
        try:
            # Connect to port 80
            host_ip = socket.gethostbyname('www.snhu.edu')
            s.connect((host_ip, port))

            # Get the input and output streams
            def getInputStream():
                for line in sys.stdin:
                    print("line %s" % line.rstrip("\n"))
            def getOutputStream():
                for line in sys.stdout:
                    print("line %s" % line.rstrip("\n"))

            # Make a request for the document specified in args[1]
            message = "GET /" + requestedDocument + " HTTP/1.1  \r\nHost: "
            + args[0] + " \r\n\r\n "
            print(message)
            flush(message)

            # Read the web server response
            line = ""
            while line != null:
                if len(line) == 0:
                    break
                print(line)
            
        #If anything is wrong, print an error message and close all streams
        except Exception as e:
            logger.error(str(e))
            os.close(0)   # close C's stdin stream
            os.close(1)   # close C's stdout stream
            os.close(2)   # close C's stderr stream