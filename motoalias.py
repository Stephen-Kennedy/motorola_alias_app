from flask import Flask, render_template
import sqlite3

app=Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

def view_command():
    for row in database.view():
        print('hello')

#if __name__=="__main__":
#    app.run(debug=True)


def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS provisioner ('radio_id_' TEXT,
        'serial_number_' TEXT, 'alias_' TEXT, 'security_' TEXT, 'capability_' TEXT,
        'site_' TEXT, 'primary_tg_' TEXT)""")
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM provisioner")
    rows=cur.fetchall()
    conn.close()
    return rows

def insert(radioid, serialnum, alias, security, capability, site, primarytg):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO provisioner VALUES (?,?,?,?,?,?,?)", (radioid, serialnum, alias, security, capability, site, primarytg))
    conn.commit()
    conn.close()

def update(radioid, serialnum, alias):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE provisioner SET serial_number_=?, alias_=? WHERE radio_id_=?", (serialnum, alias, radioid))
    conn.commit()
    conn.close()


create_table()
insert("4800000", "427xxx123", "chief1", "1", "1001", "1", "1002")
#update('480', '999', "homerun")
print(view())
