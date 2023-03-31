from email_sender import sendmail
subject=open('subject.txt','r')
subject=subject.read()
body=open('body.txt','r')
body=body.read()
emails=open('database.txt','r')
u_email = emails.readlines()
for mail_no,mail_ID in enumerate(u_email):
    sendmail(mail_ID,subject,body)
    print (f"Email no. {mail_no+1} has sent to {mail_ID}")
emails.close()