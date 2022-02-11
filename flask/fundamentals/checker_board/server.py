from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/')
def check1():
    return render_template('index.html', num1=4, num2=4, color1='red', color2='black')

@app.route('/<int:num1>')
def check2(num1):
    num1 = int(num1/2)
    return render_template('index.html', num1=num1, num2=4, color1='red', color2='black')

@app.route('/<int:num1>/<int:num2>')
def check3(num1, num2):
    num1 = int(num1/2)
    num2 = int(num2/2)
    return render_template('index.html', num1=num1, num2=num2, color1='red', color2='black')

@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def check4(num1, num2, color1, color2):
    num1 = int(num1/2)
    num2 = int(num2/2)
    return render_template('index.html', num1=num1, num2=num2, color1=color1, color2=color2)
if __name__=="__main__":    
    app.run(debug=True)    

