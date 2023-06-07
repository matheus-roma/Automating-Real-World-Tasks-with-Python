from email.message import EmailMessage
import os.path, mimetypes, smtplib, getpass, ssl
message = EmailMessage()

sender_email = "me@example.com"
receiver_email = "you@example.com"

message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Greetings from {} to {}!'.format(sender_email, receiver_email)
body = """Hey there!"""
message.set_content(body)

attachment_path = "resources/example.jpg"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,filename=os.path.basename(attachment_path))


port = 465  
app_password = input("Enter Password: ")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #server.set_debuglevel(1)
    server.login("sender@xyz.com", app_password)
    server.sendmail(sender_email, receiver_email, message)
    

#print(message)