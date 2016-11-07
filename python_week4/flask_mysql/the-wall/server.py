from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from validations import registration_validation, add_user, login_query, create_new_post, get_all_posts, get_comments_from_post, comment_on_post
from mysqlconnection import MySQLConnector

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, "the_wall")
app.secret_key = "thisisthesupersecretkey"


@app.route('/')
def index():
    if 'logged_in_user' not in session:
        flash("successfully logged out!", "session_status")
        return render_template('index.html')
    else:
        return render_template('the_wall.html')


@app.route('/register', methods=['POST'])
def register():

    errors = registration_validation(flash, request.form, mysql)

    if errors:
        print errors
        return redirect('/')
    else:
        print bcrypt
        add_user(flash, request.form, mysql, bcrypt)
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user_exists = login_query(email, password, flash, mysql)

    if user_exists:
        if bcrypt.check_password_hash(user_exists[0]['password'], password):
            session['logged_in_user'] = user_exists[0]['id']
            return render_template('the_wall.html')
        else:
            flash("incorrect email/password combo")
            return redirect('/')
    else:
        flash("incorrect email/password combo")

    return redirect('/')



@app.route('/post', methods=['POST'])
def post():

    if 'logged_in_user' in session:
        create_new_post(mysql, request.form, session['logged_in_user'])

    return redirect('/wall')


@app.route('/wall')
def wall():
    if not 'logged_in_user' in session:
        return rediret('/')
    else:
        posts = get_all_posts(mysql)
        for post in posts:
            post['comments'] = get_comments_from_post(mysql, post['id'])

        return render_template("the_wall.html", posts = posts)


@app.route('/comment', methods=['POST'])
def comment():
    if 'logged_in_user' in session:
        comment_on_post(mysql, request.form, session['logged_in_user'])

    return redirect('/wall')


@app.route('/logout')
def logout():
    if 'logged_in_user' in session:
        session.pop('logged_in_user')

    return redirect('/')




app.run(debug=True)
