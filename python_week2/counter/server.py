from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = '0'
@app.route('/', methods=['POST', 'GET'])

def index():
    if 'counter' not in session:
        session['counter'] = 0
    if request.method == 'POST':
        if request.form['addition'] == "reset":
            session['counter'] = 1
        elif request.form['addition'] == "ninjas":
            session['counter'] = int(session['counter']) + 2
        return render_template('index.html')

    elif request.method == 'GET':
        return render_template('index.html')


app.run(debug=True)
