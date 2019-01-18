import smtplib

message = """Subject: Your username for login

Hi {name}, this hospital db mailing you"""

name = "soroush"
grade = "20"
from_address = "moh.kahani@gmail.com"
email = "hosenpursoroush@yahoo.com"


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(from_address, "11kahani")
server.sendmail(from_address, email, message.format(name=name))
server.close()
print('Email sent!')

