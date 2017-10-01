from flask import Flask, redirect, request, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    if password != "" and password != " " and password == verify_password:
        if username != " " and username != "":
            if email == "":
                return redirect('/success?username=' +username)
            elif '@' and '.' in email and not " " in email:
                return redirect('/success?username=' +username)
            else:
                return render_template('login.html', username=username, email_error='Please enter a valid email') 
        else:  
            return render_template('login.html', email=email, username_error='Field cannot be left blank')
    else:
        return render_template('login.html', username=username, email=email, pw_error='Passwords do not match')

@app.route('/success', methods=['GET'])
def success():
    username = request.args.get('username')
    return render_template('success.html', username=username)
app.run()    