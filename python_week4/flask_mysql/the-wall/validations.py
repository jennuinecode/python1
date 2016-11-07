import re

######################################
# registration form validation function
def registration_validation(flash,form,mysql):

    error = False
    first_name = form['first_name']
    last_name = form['last_name']
    email = form['email']
    password = form['password']


    users = login_query(email, password, flash, mysql)

    if not first_name or not last_name:
        flash("you must enter a first and last name", "name_error")
        error = True
    if not re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        flash("please enter a valid email address", "email_error")
        error = True
    if len(password) < 8:
        flash("password must be at least 8 characters long", "password_error")
        error = True
    if users:
        flash("email is already in use, please choose another one.")


    return error

import re


def add_user(flash,form,mysql, bcrypt):
    print bcrypt
    pw_hash = bcrypt.generate_password_hash(form['password'])

    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

    data = {
        'first_name' : form['first_name'],
        'last_name'  : form['last_name'],
        'email'      : form['email'],
        'password'   : pw_hash
    }

    mysql.query_db(query, data)
    flash("success! new user created!", "success_message")


######################################
#check if user exists in database function
def login_query(email, password, flash, mysql):

    query = 'SELECT * from users WHERE users.email = :email'
    data = {
        'email': email,

    }

    existing_user = mysql.query_db(query,data)

    return existing_user


def get_all_posts(mysql):

        query = "SELECT users.first_name,users.last_name, posts.id, posts.content, posts.created_at FROM posts JOIN users ON posts.user_id = users.id"

        return mysql.query_db(query)



def create_new_post(mysql, form, logged_in_user):

    post = form['content']
    query = "INSERT INTO posts (content, user_id, created_at, updated_at) \
    VALUES (:content, :user_id, NOW(), NOW() )"

    data = {
        'content' : post,
        'user_id' : logged_in_user
    }

    mysql.query_db(query, data)


def comment_on_post(mysql, form, logged_in_user):

    comment = form['comment']
    post_id = form['post_id']
    query = "INSERT INTO comments (content, user_id, post_id, created_at, updated_at) \
    VALUES (:content, :user_id, :post_id, NOW(), NOW() )"

    data = {
        'content' : comment,
        'user_id' : logged_in_user,
        'post_id' : post_id
     }

    mysql.query_db(query, data)


def get_comments_from_post(mysql, id):

    query = "SELECT * from comments WHERE comments.post_id = :id"

    data = {
        'id': id
    }

    return mysql.query_db(query, data)
