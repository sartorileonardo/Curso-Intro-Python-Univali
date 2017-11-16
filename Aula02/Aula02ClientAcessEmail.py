#!/usr/bin/python3

import smtplib

mail = smtplib.SMTP('smtp.gmail.com', 587)

sender = 'leonardogt4@hotmail.com'
receivers = ['leonardogt4@hotmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except smtplib.SMTPException:
   print ("Error: unable to send email")
