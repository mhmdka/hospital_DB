import mysql.connector
import json

with open('../config.json') as datafile:
    config = json.load(datafile)

mydb = mysql.connector.Connect(host=config['host'], user=config['user'], passwd=config['passwd'], database=config['database'])
hospital = mydb.cursor()

