import requests
import json
import smtplib
from email.mime.text import MIMEText

gmail = 'your_gmail'
gmail_password = 'your_password'

reciever = 'recievers_email'

# how many facts to send (max 100)
amount = #

# decide how many seconds to wait between emails
sleep_seconds = 300

num = 1
r = requests.get('http://catfacts-api.appspot.com/api/facts?number=' + str(amount))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail, gmail_password)
print r.json()
for fact in r.json()['facts']:
    sleep(sleep_seconds)
    msg = MIMEText(fact)
    msg['Subject'] = 'CAT FACTZ %d' % num 
    msg['From'] = gmail  
    msg['To'] = reciever
    server.sendmail(gmail, [reciever], msg.as_string())
    num +=1
server.quit()