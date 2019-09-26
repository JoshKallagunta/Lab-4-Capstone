import chainsawDB
from chainsawDB import recordHolder
import peewee
import sqlite3

def add_record_holder(recordHolder):

    name = input('Enter a player''s name: ')
    country = input('Enter the country they are from: ')
    catches = int(input('How many catches did they have? '))

    try:
        conn.execute('insert into records value (?,?,?)', name, country, catches)
    except peewee.IntegrityError:
        print('Error, this record holder is already in the database! ')

def delete_record_holder(recordHolder):
    rows_deleted = recordHolder.delete().where(recordHolder.name == )
