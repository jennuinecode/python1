from flask import Flask, session, render_template, redirect
import random, datetime


app = Flask(__name__)
app.secret_key = "asdfjkl12347890"

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []

    return render_template('index.html')


@app.route('/process_money/<building>', methods=['GET', 'POST'])
def earn(building):

    if building == 'farm':
        earned = random.randint(10,20)
        message = 'Earned ' +str(earned)+' gold from the farm! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    if building == 'cave':
        earned =  random.randint(5,10)
        message = 'Earned ' +str(earned)+' gold from the cave! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    if building == 'house':
        earned = random.randint(2,5)
        message = 'Earned ' +str(earned)+' gold from the house! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    if building == 'casino':
        earned = random.randint(-50,50)
        message = 'Earned ' +str(earned)+' gold from the casino! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        if earned < 0:
            message = 'Lost ' +str(earned)+' gold from the casino! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    session['gold'] += earned
    session['activities'].insert(0, message)


    return redirect('/')

app.run(debug=True)
