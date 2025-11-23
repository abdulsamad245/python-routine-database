import sqlite3

def connect():
    conn=sqlite3.connect('./routine.db')
    cur=conn.cursor()
    #cur.execute('CREATE TABLE routine(id INTEGER PRIMARY KEY ,date TEXT ,earnings integer ,exercise text ,study text ,diet text ,python text) ')
    cur.execute('CREATE TABLE IF NOT EXISTS routine(id INTEGER PRIMARY KEY ,date TEXT ,earnings integer ,exercise text ,study text ,diet text ,python text) ')
    conn.commit()
    conn.close()

def insert(date ,earnings ,exercise ,study ,diet ,python ):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO routine VALUES(NULL ,?,?,?,?,?,?)',(date ,earnings ,exercise ,study ,diet ,python ))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute('SELECT *FROM routine')
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    print((rows))
    return rows

def search(date='' ,earnings='' ,exercise='' ,study='' ,diet='' ,python='' ):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM routine WHERE date=? OR earnings=? OR exercise=? OR study=? OR diet=? OR python=?' ,(date ,earnings ,exercise ,study ,diet ,python ))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM routine WHERE id=?',(id,))
    conn.commit()
    conn.close()
    
connect()
    




