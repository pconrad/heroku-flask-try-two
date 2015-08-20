import os
from flask import Flask, url_for, render_template

app = Flask(__name__)

url_for('static', filename='style.css')

@app.route('/')
def helloRoot():
    return 'Hello SPIS  Banana Pineapple!!!'

def ftoc(ftemp):
    return (ftemp - 32 ) * (5.0/9.0)
    
@app.route('/ftoc/<ftempString>')
def convertFtoC(ftempString):
    ftemp = 0.0
    try:
        ftemp = float(ftempString)
        ctemp = ftoc(ftemp)
        return "In Farenheit: " + ftempString + " In Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftempString + " to a number"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/ftocForm')
def ftocForm():
    return "stub"
