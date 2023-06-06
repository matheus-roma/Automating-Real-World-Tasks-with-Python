from email.message import EmailMessage

message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

#From, To, and Subject are examples of email header fields

#They’re key-value pairs of labels and instructions used by 
# email clients and servers to route and display the email

#They’re separate from the email's message body, which is 
# the main content of the message.

body = """Hey there!"""




print(message)