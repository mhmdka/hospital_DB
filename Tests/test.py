import mysql.connector
import json

with open('../config.json') as datafile:
    config = json.load(datafile)

mydb = mysql.connector.Connect(host =config['host'], user=config['user'], passwd=config['passwd'])


# print(mydb)


my_cursor = mydb.cursor()
# my_cursor.execute(")

id = 3
my_cursor.execute("use test")
my_cursor.execute("SELECT name FROM customers where id=%s", (id,))


print(my_cursor.fetchone()[0])


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

