from flask import Flask, render_template, request, redirect, jsonify, url_for
import threading
from login_app import start_tkinter  # Import your tkinter app start function

app = Flask(__name__)

# Home route that loads the login page (HTML form)
@app.route('/')
def home():
    return render_template('login-Copy1.html')  # This is where the login form will go

# Login route for handling POST requests for login credentials
@app.route('/login', methods=['POST'])
def login():
    # If the request has JSON data, get it
    if request.is_json:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
    else:
        # Handle form data if it's a normal POST (non-JSON)
        username = request.form['username']
        password = request.form['password']

    correct_username = 'user123'
    correct_password = 'password'

    if username == correct_username and password == correct_password:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login-Copy1.html', error="Invalid credentials, please try again.")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Show the new page after successful login

if __name__ == '__main__':
    app.run(debug=True, port=5001)






