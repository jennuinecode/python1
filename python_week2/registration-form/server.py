from flask import Flask, render_template, redirect, flash, request, session
import re
from db import readUser

app = Flask(__name__)
app.secret_key="asdkfjas;dlkfjas;ldkfjsdf"

@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html')
# END OF INDEX ROUTE

@app.route('/login', methods=['POST'])
def login():

    email = request.form['email']
    password = request.form['password']
    errors = []

    if len(email) < 1:
        errors.append("Email field cannot be blank!")

    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        errors.append("Must enter valid email!")

    if errors:
        return render_template('index.html')
# END OF LOGIN ROUTE

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')

#DND OF REGISTER ROUTE

@app.route('/create_user', methods=['POST', 'GET'])
def create_user():

    error = False
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    new_user = {
        'Name' : first_name + last_name,
        'Email': email,
        'Password' : password
    }

    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        flash("Must enter a valid email address", "email_error")
        error = True
        session['email'] = ''

    if re.search(r"[0-9]", first_name):
        flash("Name cannot have numbers", "first_name_error")
        error = True
        session['Name'] = ''

    if re.search(r"[0-9]", last_name):
        flash("Name cannot have numbers", "last_name_error")
        session['last_name'] = ''
        error = True

    if len(first_name) < 1:
        flash("Must enter your first name", "first_name_error")
        session['first_name'] = ''
        error = True

    if len(last_name) < 1:
        flash("Must enter your last name", "last_name_error")
        error = True
        session['last_name'] = ''

    if confirm_password != password:
        flash("Passwords must match! Please try retyping Password", "password_error")
        error = True

    if len(password) < 1:
        flash("Password must have atleast 8 characters!", "password_error")
        error = True

    elif len(password) < 8:
        flash("Password must have atleast 8 characters!", "password_error")
        error = True

    if error == True:
        return redirect('/register')


app.run(debug=True)
