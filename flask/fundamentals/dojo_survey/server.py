from xml.etree.ElementTree import Comment
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = ('f80df7c319a6cb1f70a84a27da80827dc309891d86dddf868df4ef69baee864a')


@app.route('/')          
def hello_world():
    return render_template('index.html') 

@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('result.html')

    
if __name__=="__main__":   
    app.run(debug=True)    
