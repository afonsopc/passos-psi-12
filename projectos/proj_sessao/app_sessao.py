from flask import Flask, session, render_template, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template("index.html", username=session.get('username'))

@app.route('/login', methods=["POST"])
def login():
    session['username'] = request.form['username']
    return render_template("index.html", username=session.get('username'))

@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html", username=session.get('username'))

if __name__ == '__main__':
    app.run()
