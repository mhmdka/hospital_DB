from packages.model import hospital
import smtplib

class Registeration:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.phone_number = 0
        self.email = ""

    def register(self):
        #TODO

    def email(self):
        message = """Subject: Your username for login

        Hi {username}, your username for login is {user_code}"""

        name = self.username
        query = "select User_Code form user where 'E-Mail'=%s"
        hospital.execute(query, (self.email,))
        user_code = hospital.fetchone()[0]

        from_address = "moh.kahani@gmail.com"
        email = self.email
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(from_address, "11kahani")
            server.sendmail(from_address, email, message.format(name=name, grade=user_code))
            server.close()
            print('Email sent!')
        except:
            print("Something went wrong :(")


