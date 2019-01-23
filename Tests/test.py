import mysql.connector
import json

with open('../config.json') as datafile:
    config = json.load(datafile)

mydb = mysql.connector.Connect(host =config['host'], user=config['user'], passwd=config['passwd'])


# print(mydb)


my_cursor = mydb.cursor()
# my_cursor.execute(")
my_cursor.execute("use Hospital_DB")
my_cursor.execute("select date_appointment,time_appointment,Doctor_UserCode,Username,Patient_UserCode from appointment, user where appointment.Doctor_UserCode = user.User_Code;")
doctors = my_cursor.fetchall()
print(doctors)
# id = 3
# my_cursor.execute("use Hospital_DB")
# try:
#     my_cursor.execute("insert into user(Username,user_password,Phone_Number,`E-Mail`,isVerified) values('ali',234567,252345,'afshinshah77@gmail.com',0)")
# except Exception as e:
#     print(e)

# my_cursor.execute("SELECT Role_Name FROM role where id=%s", (id,))
mydb.commit()

print(my_cursor.fetchone())



# my_cursor.execute("create table customers (id int auto_increment primary key,
#  name varchar(40) not null, address varchar(255))")


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# my_cursor.executemany(sql, val)

#
# customers = my_cursor.fetchall()
# print(customers)

# mydb.commit()

# print(my_cursor.rowcount, "record inserted.")



# my_cursor.execute("CREATE TABLE customers (id int, address VARCHAR(255))")


