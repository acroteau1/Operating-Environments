# 
# This program is a very simple web server. When it receives a HTTP request,
# it just sends the request back to the client. The default port this
# server listens to is 1500.
#
# Usage:
# 
# python HttpRequestMirror <port>
#
#

# Import the relevant packages
import sys
import io
import socket

# Create HttpRequestMirror class
class HttpRequestMirror():
    # Get the port to listen on
    def IO_exception(*args):
        PORT = 1500
        result = args[0]
        for x in args:
            if x == 1:
                PORT = parse(args[0])
    try:
        # Create a server socket
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.bind((socket.gethostname(), 1500))
        print("Server bound at port " + ss.getsockname()[1])

        while true:
            (clientsocket, address) = ss.accept()
            # Get input and output streams to talk to the client from the socket
            def getInputStream():
                for line in sys.stdin:
                    print("line %s" % line.rstrip("\n"))
            def getOutputStream():
                for line in sys.stdout:
                    print("line %s" % line.rstrip("\n"))
            # Start sending our reply
            print("HTTP/1.1 200 ")
            print("Content-Type: text/plain")
            print()
            flush()

            # Read the HTTP request from the client, and echo it back to the client
            line = ""
            while line != null:
                if len(line) == 0:
                    break
                print(line)
            
            # Close the connection and resume waiting for additional connections
            os.close(0)   # close C's stdin stream
            os.close(1)   # close C's stdout stream
            ss.close()    # close the client

    # Output an error message in the case of an exception
    except Exception as e:
        print(str(e))
        print("Usage: python HttpRequestMirror <port>")