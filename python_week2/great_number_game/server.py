from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "This is secret_key"

@app.route('/', methods=['POST', 'GET'])
@app.route('/guess', methods=['POST', 'GET'])
def index():
    if 'answer' not in session:
        # correct_guess = random.randrange(0,101)
        correct_guess = 10
        if request.method == 'POST':
            if int(request.form['guess']) == correct_guess:
                session['answer'] = "Good Job!"

            elif int(request.form['guess']) > correct_guess:
                session['answer'] = "Your guess is too high!"
            else:
                session['answer'] = "Your guess is too low!"
        return render_template('index.html')

# ADD RESET ROUTE
app.run(debug=True)
