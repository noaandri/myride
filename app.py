from flask import Flask, render_template, redirect, url_for, request, session, flash
import os
import json
from werkzeug.security import generate_password_hash, check_password_hash
from config import secret_key

app = Flask(__name__)
app.secret_key = secret_key
users_folder = 'users'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        user_data = {
            'email': email,
            'password': hashed_password
        }

        with open(os.path.join(users_folder, f"{email}.json"), 'w') as f:
            json.dump(user_data, f)

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user_file = os.path.join(users_folder, f"{email}.json")
        if os.path.exists(user_file):
            with open(user_file, 'r') as f:
                user_data = json.load(f)

            if check_password_hash(user_data['password'], password):
                session['user'] = email
                flash('Login erfolgreich!', 'success')
                return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Erfolgreich ausgeloggt.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Bitte logge dich zuerst ein.', 'danger')
        return redirect(url_for('login'))

    user_file = os.path.join(users_folder, f"{session['user']}.json")
    with open(user_file, 'r') as f:
        user_data = json.load(f)

    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True, port=5005)
