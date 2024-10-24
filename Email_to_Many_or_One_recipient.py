import smtplib

sender_email ="tanyi_daniel@yahoo.com"
rec_email ="dtarh@yahoo.com"
password =input(str("Please enter your password: "))
message = "Hey , This is Daniel your colleaque."

server = smtplib.SMTP("smtp.yahoomail.com",587)
server.starttls()
server.login(sender_email,password)
print("Login Sucess")
server.sendmail(sender_email,rec_email,message)
print("Email has been sent to", rec_email)
server.close()
print("Server Closed")