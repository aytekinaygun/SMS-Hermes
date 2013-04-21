#!/usr/bin/python

import sys, httplib

# I use the URL of the SMS service. 
# You enter the URL that you are using.
HOST = "processor.smsorigin.com"
API_URL = "/xml/process.aspx"

def do_request(xml_location):
        request = xml_location
        webservice = httplib.HTTP(HOST)
        webservice.putrequest("POST", API_URL)
        webservice.putheader("Host", HOST)
        webservice.putheader("User-Agent","Python post")
        webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
        webservice.putheader("Content-length", "%d" % len(request))
        webservice.endheaders()
        webservice.send(request)
        statuscode, statusmessage, header = webservice.getreply()
        result = webservice.getfile().read()
        print statuscode, statusmessage, header
        print result
