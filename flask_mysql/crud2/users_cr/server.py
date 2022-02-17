from flask import Flask, render_template, request, redirect

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("read.html",users=User.get_all())


@app.route('/users/new')
def new():
    return render_template("create.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/users/<int:id>')
def showuser(id):
    data ={ 
        "id":id
    }
    return render_template("user.html",user=User.get_one(data))

@app.route('/users/<int:id>/edit')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edituser.html",user=User.get_one(data))

@app.route('/users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)
