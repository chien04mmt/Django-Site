

# import smtplib
# smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
# #!/usr/bin/python

from importlib.resources import contents
from multiprocessing import context
import smtplib

sender = 'cncs-vn-code@mail.foxconn.com'
receivers = ['cncs-vn-code@mail.foxconn.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
context={
   'mailto':'cncs-vn-code@mail.foxconn.com',
  'from':'cncs-vn-code@mail.foxconn.com',
   'cc':'',
   'subject':'TEST3',
   'msg':message
}
try:
   smtpObj = smtplib.SMTP('http://10.224.69.51/SMTPService/SMTPService.asmx/WMSendMail')
   smtpObj.sendmail(sender, receivers, context)         
   print ("Successfully sent email")
except:
   print ("Error: unable to send email")