from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "This_Is_Secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitted', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('submitted.html' ,name = session['name'], location = session['location'], language = session['language'], comment = session['comment'])





app.run(debug=True)
