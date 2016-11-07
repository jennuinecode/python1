from flask import Flask, render_template
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, "emails")


@app.route('/')
def index():


    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():

    emails = mysql.query_db('SELECT * FROM emails')
    return render_template('success.html', emails = emails)


app.run(debug=True)
