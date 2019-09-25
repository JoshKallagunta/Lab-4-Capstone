#Josh Kallagunta
import sqlite3

#Creating the db file 
conn = sqlite3.connect('lab_4_db.db')

#Creating records table if it does not exists
conn.execute('create table if not exists records (name text, country text, catches intiger)')

#Getting user data tp populate the table 
name = input('Enter a player''s name: ')
country = input('Enter the country they are from: ')
catches = int(input('How many catches did they have? '))

#Insert statement using permaters 
conn.execute('insert into records value (?,?,?)', name, country, catches)

#Saving the changes
conn.commit()

#Displaying the stored results 
displayStoredResults = conn.execute('select * from records')

#Printing the data from the table 
for row in displayStoredResults:
    print(row)

conn.close()

