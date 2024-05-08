from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define login details
login_details = {
    'username': 'praveen',
    'password': 'portfolio'
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if username == login_details['username'] and password == login_details['password']:
        # Successful login, redirect to welcome page
        return redirect(url_for('welcome', username=username))
    else:
        # Invalid credentials, redirect back to login page
        return redirect(url_for('login'))

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

@app.route('/resume')
def resume():
    return redirect(url_for('static', filename='Praveen Resume.docx'))

if __name__ == '__main__':
    app.run(debug=True)
