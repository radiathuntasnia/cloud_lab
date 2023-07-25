from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_mysql_database'
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()

    if user:
        return "Login successful"
    else:
        return "Invalid username or password"


if __name__ == '__main__':
    app.run()
