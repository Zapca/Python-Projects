import json
import sqlite3

conn=sqlite3.connect('roaster.sqlite')
cur=conn.cursor()

cur.executescript('''
                  
DROP TABLE IF EXISTS User ;
DROP TABLE IF EXISTS Member ;
DROP TABLE IF EXISTS Course ;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE     
);
                  
CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);
                  
CREATE TABLE Member(
    User_id INTEGER,
    Course_id INTEGER,
    Role INTEGER ,
    PRIMARY KEY (User_id,Course_id)
)
''')

fname=input('Enter a file name: ')
if len(fname)<1: fname='roaster.json'

fhand=open(fname).read()
data=json.loads(fhand)

for array in data:

    User_name=array[0]
    Course_title=array[1]
    role=array[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(User_name,))
    cur.execute('SELECT id FROM User WHERE name=?',(User_name,))
    User_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(Course_title,))
    cur.execute('SELECT id FROM Course WHERE title=?',(Course_title,))
    Course_id=cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member(User_id,Course_id,Role) VALUES(?,?,?)',(User_id,Course_id,role))

    conn.commit()

conn.close()