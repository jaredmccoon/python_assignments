from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)    
app.secret_key = ('8fe3927426f966339b87fb39ffda35494bfa6157ea88927f5c938bac320aff8b')


@app.route('/', methods=['POST', 'GET'])          
def hello_world():
    
    # if request.method == 'POST':
        
    return redirect('/counter') 

@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')


@app.route('/destroy_session', methods=['POST'])
def remove():
    del session['count']
    if 'count' in session:
        session['count'] = 0
    return redirect('/counter') 


@app.route('/counter')
def newcount():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/count2')
def doublecount():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 2
    return render_template('index.html')

if __name__=="__main__":       
    app.run(debug=True)   