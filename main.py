from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_signup():
    return render_template('main.html')

@app.route('/error', methods=['POST', 'GET'])
def validate_user_info():


    username=request.form['username']
    username_error= ""
    
    if username == "":
        username_error="Please enter username"

    elif " " in username:
        username_error="Username cannot contain spaces"
    
    elif len(username) < 3 or len(username) > 20:
        username_error="Username must containg beween 3 and 20 characters"
     


    password=request.form['password']
    password_error=""
    if password == "":
        password_error="Please enter password"
    
    elif " " in password:
        password_error="Password cannot contain spaces"

    elif len(password)<3 and len(password)>20:
        password_error="Password must be between 3 and 20 characters"
      


    password=request.form['password']
    verify=request.form['verify']
    verify_error=""
    if password=="":
        verify_error="Please verify password"

    elif verify not in password:
        verify_error="Passwords do not match"
 

    email_error=""
    email=request.form['email']
    valid_email=re.compile("[a-zA-Z0-9_]+\.?[a-zA-Z0-9_]+@[a-z]+")
    
    if valid_email.match(email):
        return True
    else:
        email_error="Please enter valid email or leave blank"
       


    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username)) 
    else:
        return render_template('main.html',
            username=username,
            username_error=username_error, 
            password=password, 
            password_error=password_error,
            verify=verify,
            verify_error=verify_error, 
            email=email, 
            email_error=email_error)   
    




@app.route('/welcome')
def display_welcome():
    username=request.args.get('username')
    return render_template('welcome.html', username=username) 


app.run()