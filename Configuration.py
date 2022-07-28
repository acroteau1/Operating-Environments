# 
# XML parser for configuration parameters
# 
# You can use this file with your web server.
# 
# This maps configuration parameters to a HashMap and are retrieved
# through the following getter methods in the "Test" file:
# 
# getLogFile()
# getDocBase()
# getServerName()
# 
# @author Alison Croteau
# Original Java file by Gagne, Galvin, Silberschatz
# Operating System Concepts with Java - Eighth Edition
# Copyright John Wiley & Sons - 2010
# 

# Import relevant packages
import xml
import xml.sax
import xml.sax.handler
from xml.sax.handler import ContentHandler
import xml.parsers.expat
from xml.dom.minidom import parse, parseString
import socket
from xml.sax import saxutils
import itertools
import sys
from typing import Dict, Tuple
from xml.etree import ElementTree
from xml.sax.saxutils import XMLGenerator
from xml.sax.xmlreader import AttributesNSImpl

# Declare Configuration class
class Configuration():
# No need to declare variables, they are declared when value is assigned
    def publish(self, handler):
        self.handler = handler

    # Create file for the referenced configuration file, enable program to write to file
    cf = open("configurationFile", "w")
    # Implement ContentHandler interface by writing SAX events into an XML document
    x = saxutils.XMLGenerator()
    # Write to the document in the case of a configuration exception
    x.startDocument()
    def raise_configuration_exception():
        def __init__(self, configurationFile):
            self.configurationFile = configurationFile
        
        try:
        # Use the default (non-validating) parser
            parser = xml.sax.make_parser()

        # Parse the Input
            parser.parse(open(configurationFile, "a"), self)
        # Write in contingency instructions for SAX parse exceptions, SAX exception, and I/O exception
        except:
            parser_config_exception = xml.sax.SAXParseException(
                "Parser Configuration Exception",
                None, self._locator)
            self.getErrorHandler().error(parser_config_exception)
            sax_exception = xml.sax.SAXException(
                "SAX Exception")
            self.getErrorHandler().error(sax_exception)
        # True I/O Exception not supported. Closest SAX exception used instead. 
            IO_exception = xml.sax.SAXNotRecognizedException(
                "SAX not recognized")
            self.getErrorHandler().error(IO_exception)
        
    #Map each configuration attribute to its value
    lName = "string"
    qName = "string"
    attrs = AttributesNSImpl({}, {})
    x.startElementNS(lName, qName, attrs)
    
    # Map element name to the lName string, or qName is lName is blank    
    elementName = lName(i)
    if elementName == "":
        elementName = qName
        
    # Get the attributes associated with the element
    if attrs != null:
        array = range(attrs)
        for i in range(len(array)) :
            aName = attrs.localname(i)
            if aName == "":
                aName = attrs.getQname(i)

    #map the element and attribute to its value
    config_map = HashMap()
    config_map.put(elementName + "." + aName, attrs.getValue(i))

    # End writing the elements and document
    x.endElement('elems')
    x.endDocument()

    # Returns the location of the log file
    def getLogFile():
        return map.get("logfile.log")

    # Returns the location of the document base
    def getDocBase():
        return map.get("context.docBase")

    # Returns the name of the server
    def getServerName():
        print(socket.gethostname())