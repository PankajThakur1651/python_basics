import smtplib
from email.mime.text import MIMEText

body = "This is a test mail, how are you ?"

msg = MIMEText(body)
msg['From'] = 'pankaj.thakur1651@gmail.com'
msg['To'] = 'pankaj.thakur1651@gmail.com'
msg['Subject'] = 'Hello'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('pankaj.thakur1651@gmail.com', 'ktwootqmuvlmngxw')
server.send_message(msg)

print('Mail sent')
server.quit()
