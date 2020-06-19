from flask import Flask, render_template, request, session, url_for, redirect
import bcrypt
from datetime import datetime 

from flask_pymongo import PyMongo
from mongoengine import connect

from User import User
from registerForm import register
from loginForm import loginForm


app = Flask(__name__)
app.secret_key = 'development key'
app.config['MONGO_URI'] = "mongodb://localhost:27017/Person"
app.config['MONGO_DBNAME'] = "Person"
mongo = PyMongo(app)



connect('Person',host='localhost',port=27017)
@app.route('/')
def index(): 
    #loggedIn = True
    return render_template('base.html')


@app.route('/home', methods=['GET', 'POST'])
def home_form():
    if request.method == 'POST':

        return redirect(url_for('base'))

    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = register()
    if request.method == 'POST':
         user = mongo.db.Person
         existing_user = user.find_one({'email': request.form['email']})

         if existing_user is None:
             password = request.form.get('password')
             confirmPassword = request.form.get('confirm')
             if len(password) >= 6:
                 if password is not confirmPassword:
                      user = User(
                       firstname=request.form.get("firstname"),
                       lastname=request.form.get("lastname"),

                       birthdate=datetime.strptime(
                           request.form.get("birthdate"), '%Y-%m-%d'),
                       email=request.form.get("email"),
                       password=bcrypt.hashpw(request.form.get(
                           "password").encode('utf-8'), bcrypt.gensalt())

                        )
                      user.save()
                      return 'you have successfully registerted,'
                 return 'Passwords must match!'
             return 'Passwords length must greater than 5!'
         return 'That username already exists!'
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if request.method == 'POST':

        user = mongo.db.user
        login_user = user.find_one({'email': request.form.get('email')})
        

        if login_user:
                    if bcrypt.checkpw(request.form.get('password').encode('utf-8'), login_user['password'].encode('utf-8')):
                        session['email'] = request.form['email']
                        loggedIn = None
                        userInfo = {
                            'firstname': login_user['firstname'],
                            'lastname': login_user['lastname'],
                            'email':  login_user['email'],
                        }
                        return render_template('profil.html', **userInfo)

        return 'Invalid email/password combination'
    return render_template('login.html')   




if __name__ == "__main__":
    app.run(debug=True)
