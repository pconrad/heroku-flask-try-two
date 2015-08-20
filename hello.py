import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
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

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/ftocForm')
def ftocForm():
    return "stub"
