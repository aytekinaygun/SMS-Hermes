#!/usr/bin/python
import send_sms
# -*- coding: utf-8 -*-

USER = "username"
PASSWORD = "password"
NUMBER = "telephone_number"

# Write message to be sent.
message = """
The first message from the SMS-Hermes..."""

# Control of up to 160 characters.
RESULT_MESSAGE = message[0:160]

# Create XML
# Use may vary according to the service.
SMS_XML = """
<?xml version="1.0" encoding="utf-8" ?>
<MainmsgBody>
<Command>0</Command>
<PlatformID>1</PlatformID>
<ChannelCode>570</ChannelCode>
<UserName>%s</UserName>
<PassWord>%s</PassWord>
<Mesgbody>%s</Mesgbody>
<Numbers>%s</Numbers>
<Type>1</Type>
<Originator></Originator>
</MainmsgBody>""" % (USER,PASSWORD,RESULT_MESSAGE,NUMBER) 
    
# XML files are sent as a parameter to the function.
send_sms.do_request(SMS_XML)
    
exit ()
