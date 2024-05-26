from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    ##name="Noa Roth"
    return render_template("index.html")

@app.route('/page1')
def hi():
    ##name="Page1"
    return render_template("Page1.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Daten aus dem Formular erfassen
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Überprüfen, ob Passwörter übereinstimmen
        if password != confirm_password:
            flash('Passwörter stimmen nicht überein', 'error')
            return redirect(url_for('register'))

        # Überprüfen, ob die E-Mail bereits registriert ist
        if email in users:
            flash('E-Mail bereits registriert', 'error')
            return redirect(url_for('register'))

        # Passwort hashen und Benutzer speichern
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users[email] = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'birthdate': request.form['birthdate'],
            'address': request.form['address'],
            'place': request.form['place'],
            'city': request.form['city'],
            'email': email,
            'password': hashed_pw
        }
        session['user'] = email  # Speichern der E-Mail in der Session
        return redirect(url_for('profile'))  # Weiterleitung zur Profilseite
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        user = users.get(email)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['user'] = email
            flash("Sie sind erfolgreich eingeloggt.", "success")
            return redirect(url_for('profile'))
        else:
            flash("Ungültige Anmeldeinformationen. Bitte versuchen Sie es erneut.", "error")
            return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
