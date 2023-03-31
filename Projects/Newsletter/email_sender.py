import smtplib
from email.mime.text import MIMEText
def sendmail(recipient_email, subject, body):
  sender_email = "anshbhardwajapi@gmail.com"
  sender_password = "balrsrqqyzgchjbw"
  html_message = MIMEText(body, 'html')
  html_message['Subject'] = subject
  html_message['From'] = sender_email
  html_message['To'] = recipient_email
  
  print (html_message.as_string())

  print (html_message)

  print (html_message.as_bytes())

  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login(sender_email, sender_password)
  server.sendmail(sender_email, recipient_email, html_message)
  server.quit()
sendmail('anshbhardwaj119@gmail.com','Test','Hello World')