#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# send mail from gmail address
def send_email(message):
    sender = '[theSender]@gmail.com'  
    receivers  = '[theReceiver(s)]@gmail.com'

    # content of the message
    msg = MIMEMultipart()
    msg['Subject'] = 'There was a reply!'
    msg['From'] = sender
    msg['To'] = receivers 
    content = MIMEText(message, 'plain')
    msg.attach(content)
    composed = msg.as_string()
      
    # set necessary credentials  
    username = sender  
    password = '[yourPassword]'  
      
    # send mail
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)  
    server.sendmail(sender, receivers, composed)  
    server.quit()  

site = "[stack overflow url with no replies]"
page = urllib2.urlopen(site)
soup = BeautifulSoup(page)
if soup.find_all("div", "no-answers") == []:
    send_email(site)
