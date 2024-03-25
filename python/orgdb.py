import sqlite3 as sq

conn=sq.connect('orgdb.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

user_input=input('Enter a filename: ')
if len(user_input)<1:user_input='mbox.txt'

file=open(user_input)
for line in file:
    if not line.startswith('From '):continue
    email=line.split()[1]
    org=email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org=?',(org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org,count) VALUES (?,?)',(org,1))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org=?',(org,))
conn.commit()

list=cur.execute('SELECT * FROM Counts ORDER BY count DESC LIMIT 10')

for i,j in list:
    print(i,j)

conn.close()