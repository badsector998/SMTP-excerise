from cgitb import text
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# sender = 'indahpuspitasari@gmail.com'
# receipent = ['ikhsanaprilito@gmail.com']

#setup sender and receiver
print("setup sender and receiver")
sender_email = 'aprilito.ikr@gmail.com'
sender_pass = '-'
receiver_address = "harddiskkosong@gmail.com"

#setup messages
mail_content = """

From : <%s>
To : <%s>
Subject  : I'm so sorry

I'm so sorry that i left you. I hope we can be together again.

With warm heart,
Indah

"""%(sender_email, receiver_address)

#setup MIME
print("setup MIME")
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_address
message['Subject'] = "Test mail from python3 SMTP - SIB"

#body and attachments for the mail
print("setup body and attachments")
message.attach(MIMEText(mail_content, 'plain'))

#create SMTP session for sending mail
print("setup SMTP session then sending email")
session = smtplib.SMTP('smtp-relay.sendinblue.com', 587) #uses gmail with port
session.starttls()
session.login(sender_email, sender_pass)
text = message.as_string()
session.sendmail(sender_email, receiver_address, text)
session.quit()
print('mail sent')



# try:
#     smtObj = smtplib.SMTP('localhost', 1025)
#     smtObj.sendmail(sender, receipent, message)

#     print("email sent succesfully")

# except Exception as e:
#     print(str(e))
#     print("failed to send email.")