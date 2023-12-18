import flask
import sqlite3
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

DATABASE = "database.db"

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def list_users():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users;
    """)
    users = cursor.fetchall()
    print(users)
    conn.close()
    return flask.render_template("list_users.html", users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        email = flask.request.form['email']
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, email) VALUES (?, ?);
        """, (name, email))
        conn.commit()
        conn.close()
        return flask.redirect('/')
    return flask.render_template("add_user.html")


if __name__ == "__main__":
    create_table()
    app.run()
