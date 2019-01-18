from packages.model import hospital


class Login:

    def __init__(self):
        self.usercode = 0
        self.password = 0

    def set_user(self, username, password):
        self.usercode = username
        self.password = password

    def check_authentication(self):
        hospital.execute("select User_Code from user where user.User_Code=%s and user.user_password=%s",
                         (self.usercode, self.password))
        user = hospital.fetchone()
        if user:
            hospital.execute("select Role_Name from user natural join user_role where user_Code = %s", (self.usercode,))
            role = hospital.fetchone()[0]
            # TODO
            if role:
                if role == "admin":
                # go to admin page
                if role == "patient":
                # go to patient page
                elif role == "doctor":
                # go to doctor page
                elif role == "nurse":
                # go to nurse page
                elif role == "receptionist":
                # go to receptionist page
                elif role == "accountant":
                # go to accountant page
                elif role == "pharmacist":
                # go to pharmacist page
                elif role == "Lab_Staff":
                #go to lab staff page
            else:
                print("You are not authorized yet wait for Admin to activate your account!!!")
        else:
            print("Authentication failed!\n Wrong username or password!")
