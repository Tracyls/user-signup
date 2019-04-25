from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')

def index():
    return render_template('main.html')

def is_valid_email(address):
    if len(address) < 3 or len(address) > 20:
        return False

    at = "@"
    at_count = address.count(at)
    if at_count != 1:
        return False

    period = "."
    period_count = address.count(period)
    if period_count != 1:
        return False

    space = " "
    space_count = address.count(space)
    if space_count != 0:
        return False

    else:
        return True

    

@app.route('/main', methods=['POST', 'GET'])

def validate_user_info():
    username=request.form['username']
    username_error= ""
    
    if username == "":
        username_error="Please enter username"

    if " " in username:
        username_error="Username cannot contain spaces"
    
    if len(username) < 3 or len(username) > 20:
        username_error="Username must containg beween 3 and 20 characters"
     


    password=request.form['password']
    password_error=""
    if password == "":
        password_error="Please enter password"
    
    if " " in password:
        password_error="Password cannot contain spaces"

    if len(password)<3 and len(password)>20:
        password_error="Password must be between 3 and 20 characters"
      


    password=request.form['password']
    verify=request.form['verify']
    verify_error=""
    if verify=="":
        verify_error="Please verify password"
    
    if " " in verify:
        verify_error="Cannot contain spaces"

    if verify not in password:
        verify_error="Passwords do not match"
 

    email=request.form['email']
    email_error=""
    if len(email) != 0:
        if is_valid_email(email) == False:
            email_error = "Please enter a valid email or leave blank"
            


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
    




@app.route('/welcome', methods=['GET'])
def display_welcome():
    username=request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()