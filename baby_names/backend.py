import random, string, sqlite3

def connect():
    conn=sqlite3.connect("babies.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS babies(id INTEGER PRIMARY KEY, name text, gender text, submitted_by text)")
    conn.commit()
    conn.close()
 

def insert(name,gender,submitted_by):
    conn=sqlite3.connect("babies.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO babies VALUES(NULL,?,?,?)",(name,gender,submitted_by))
    conn.commit()
    conn.close()

def search(name="",gender="",submitted_by=""):
    conn=sqlite3.connect("babies.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM babies WHERE name=? OR gender=? OR submitted_by=?",(name,gender,submitted_by))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    print rows
    return rows

def generateNewName(ls,firstLetter):
    global name 
    name = firstLetter

    for i in range(0,ls):
        i = random.choice(string.ascii_lowercase)
        if i == firstLetter:
            pass
        name+= i
    print name
    return name

def insertGeneratedName():
    insert(name,"Unisex","user")

#generateNewName(5,"M")