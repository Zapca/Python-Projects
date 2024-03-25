import sqlite3
import xml.etree.ElementTree as ET 

conn=sqlite3.connect('track.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;
            
CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE, count INTEGER ,
    rating INTEGER , len INTEGER ,
    album_id INTEGER , genre_id ,
    released_year INTEGER 
);
''')

fname=input('Enter file name: ')
if len(fname) < 1 : fname='tracks.xml'
       
def lookup(d,key):
    Mylife=False 
    for child in d:
        if Mylife: return child.text
        if child.tag=='key' and child.text==key:
            Mylife=True
    return None

stuff=ET.parse(fname)
all=stuff.findall('./dict/dict/dict')
print('Disc count',len(all))

for entry in all:
    if (lookup(entry,'Track ID') is None) : continue

    title=lookup(entry,'Name')
    count=lookup(entry,'Play Count')
    rating=lookup(entry,'Rating')
    len=lookup(entry,'Total Time')
    released_year=lookup(entry,'Year')
    artist=lookup(entry,'Artist')
    album=lookup(entry,'Album')
    genre=lookup(entry,'Genre')

    if title is None or artist is None or album is None or genre is None : 
        continue

    print(title,album,artist,genre,released_year)

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
    cur.execute('SELECT id FROM Artist WHERE name=?',(artist,))
    artist_id=cur.fetchone()[0]


    cur.execute('INSERT OR IGNORE INTO Album (title,artist_id) VALUES (?,?)',(album,artist_id))
    cur.execute('SELECT id FROM Album WHERE title=?',(album,))
    album_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name=?', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Track(title,rating,len,count,album_id,genre_id,released_year) VALUES (?,?,?,?,?,?,?)',
                (title,rating,len,count,album_id,genre_id,released_year))
    
    conn.commit()
conn.close()