import sqlite3 as sql
import bcrypt
import html


def insertUser(
    username,
    password,
):
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO users (username,password) VALUES (?,?)",
        (
            username,
            hashed,
        ),
    )
    con.commit()
    con.close()


def retrieveUsers(username, password):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    if row is None:
        con.close()
        return False
    hashed = row[0]
    if bcrypt.checkpw(password.encode("utf-8"), hashed):
        con.close()
        return True
    con.close()
    return False


def insertFeedback(feedback):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO feedback (feedback) VALUES (?)", (feedback,))
    con.commit()
    con.close()


def listFeedback():
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM feedback").fetchall()
    con.close()
    f = open("templates/partials/success_feedback.html", "w")
    for row in data:
        f.write("<p>\n")
        f.write(html.escape(str(row[1])))  # Escape to prevent XSS
        f.write("</p>\n")
    f.close()
