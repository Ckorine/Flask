from flask import Flask, render_template, request, session, url_for, redirect
#import bcrypt


app = Flask(__name__)



@app.route('/')
def index():
 return render_template('base.html')



@app.route('/home', methods=['GET', 'POST'])
def home_form():
    if request.method == 'POST':
       
        return redirect(url_for('base'))

    
    return render_template('home.html') 


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    
    if request.method == 'POST':
        #user = mongo.db.user
        #login_user = user.find_one({'username':request.form.get('username')})
        #loggedIn = None
       #if login_user:
                    #if bcrypt.checkpw(request.form.get('password').encode('utf-8'), login_user['password'].encode('utf-8')): 
                        #session['username'] = request.form['username']
                        #return render_template('login.html',**'You are logged in as ' + session['username'])
            return render_template('login.html')

    
    return  'Invalid username/password combination'


#run    

if __name__ == "__main__":
    app.run(debug=True)