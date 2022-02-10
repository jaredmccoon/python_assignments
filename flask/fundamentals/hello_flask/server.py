from flask import Flask  
app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return 'Hello World!' 
if __name__=="__main__":   




    @app.route('/<name>') 
    def hello(name):
        return name

@app.route('/say/<name>') 
def hi_name(name):
    return "Hi " + name + "!"


@app.route('/repeat/<int:num>/<name>')
def repeat(num, name):
    return num * name

app.run(debug=True)   