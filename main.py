from flask import Flask, render_template, request, redirect
import cgi



app = Flask(__name__) 
app.config['DEBUG'] = True 



@app.route("/") 
def displaysignup(): 
    return render_template('home.html') 


@app.route("/", methods= ['POST']) 
def validate(): 
    username = cgi.escape(request.form['username']) 
    password = cgi.escape(request.form['password']) 
    verifypassword = cgi.escape(request.form['verify']) 
    email = cgi.escape(request.form['email']) 
    
    usernameerror = "" 
    passworderror = "" 
    verifyerror = "" 
    emailerror = "" 


    if  len(username) == 0: 
        usernameerror = "Username required field" 
    elif len(username) > 20 or len(username) < 3: 
        usernameerror = "Username must be between 3 and 20 characters" 



    if len(password) == 0: 
        passworderror = "Password required field" 
    elif len(password) > 20 or len(password) < 3: 
        passworderror = "Password must be between 3 and 20 characters" 


    if len(verifypassword) == 0: 
        verifyerror = "Must verify password" 
    elif password != verifypassword: 
        verifyerror = "Password does not match" 


    if len(email) > 0: 
        if len(email) > 20 or len(email) < 3: 
            emailerror = "Password must be between 3 and 20 characters" 
        elif email.count("@") < 1: 
            emailerror = "at least 1 @ key allowed" 
        elif email.count("@") > 1: 
            emailerror = "only 1 @ key allowed"
        elif email.count(".") < 1: 
            emailerror = "only 1 . allowed" 
        elif email.count(" ") > 0: 
            emailerror = "remove all spaces" 
        



    if not usernameerror and not passworderror and not verifyerror and not emailerror: 
        return redirect('/welcome?username= {0}'.format(username)) 
         
    else: 
        return render_template('home.html',  
            username= username, usernameerror= usernameerror,  
            passworderror= passworderror, verifyerror= verifyerror, 
            email= email, emailerror= emailerror) 
 
 
 
 
@app.route('/welcome') 
def welcome(): 
    username = request.args.get('username') 
    return render_template('welcome.html', username= username) 
 
 
  

if __name__ == '__main__':
    app.run()