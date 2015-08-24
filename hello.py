import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def helloRoot():
    return "Try <a href='" + url_for('tempConvert') + "'>Temperature Conversion</a>"

def ftoc(ftemp):
    return (ftemp - 32 ) * (5.0/9.0)

@app.route('/tempConvert')
def tempConvert():
    return render_template('tempConvert.html')

@app.route('/doTempConvert')
def doTempConvert():

    try:

        ftemp=float(request.args['potato']);
        ctemp=ftoc(ftemp)
        return render_template('tempConvertResult.html',
                               showFtemp=ftemp,
                               showCtemp=ctemp)
    except ValueError:
        return "bar"
        return render_template('couldNotConvert.html',
                               showFtemp=ftemp);
    
if __name__=="__main__":
    app.run(debug=False)
