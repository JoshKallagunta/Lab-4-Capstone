#Josh Kallagunta
import sqlite3
from peewee import fn
from peewee import *

#Creating the db file 
conn = sqlite3.connect('lab_4_db.db')

class recordHolder():

    #A record holder's info in the DB 
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = conn
        constraints = [SQL('UNIQUE( name COLLATE NOCASE, country COLLATE NOCASE )')]

    def __str__(self):
        return f'Name: {self.name}, Country: {self.country}, Number of Catches: {self.catches}'



conn.connect()

#Creating records table if it does not exists
conn.execute('create table if not exists records (name text, country text, catches integer)')



