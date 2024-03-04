import smtplib

sender = input("Enter Sender Email :- ")
receiver = input("Enter Receiver Email :- ")
password = input("Enter Password to send Mail :- ")
subject = input("Enter Subject of Mail :- ")
text = input("Enter msg to send :- ")
msg = 'Subject: {}\n\n{}'.format(subject,text)


server = smtplib.SMTP("smtp.gmail.com")
server.starttls()
server.login(sender,password)
print("Login Success")
server.sendmail(sender, receiver, msg)
print("Mail Send Successfully to ", receiver)

