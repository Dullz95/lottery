import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# s = smtplib.SMTP('smtp.gmail.com',587)
sender_email_id = 'abdullahtest585@gmail.com'
reciever_email_id = \
f = open('PlayerID.txt','+r')
line = f.readlines()[2]
line[6:len(line)]
content =f.read()
password = "testing0909"

# subject = "Hello All"
# msg = MIMEMultipart()
# msg ['from'] = sender_email_id
# msg ['To'] = reciever_email_id
# msg ['Subject'] = subject
# body = "Hi guys how are you"
# body = body + "How was your task yesterday"
#
# msg.attach(MIMEText(body, 'plain'))
# text = msg.as_string()
# s.starttls()
# s.login(sender_email_id,password)
#
# s.sendmail(sender_email_id,reciever_email_id, text)
# s.quit()