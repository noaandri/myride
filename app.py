from flask import Flask, render_template, redirect, url_for, request, session
import os
import json
from werkzeug.security import generate_password_hash, check_password_hash
from config import secret_key
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)
app.secret_key = secret_key # Setzt secret key für aktuelle Sitzung 
users_folder = 'users' # Ordner für Userdaten

# Route für Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Route für Registrierung
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password) # Generiert gehashtes Passwort (auch wenn es nicht um sensible Daten geht, sollen Passwörter nicht im Klartext gespeichert werden)

        # Erstellt eine User mit den Benutzerdaten 
        user_data = {
            'email': email,
            'password': hashed_password,
            'activities': [],
            'weekly_goal': {
                'type': None,
                'value': 0
            }
        }

        # Speichert die Userdaten in einer JSON-Datei
        with open(os.path.join(users_folder, f"{email}.json"), 'w') as f:
            json.dump(user_data, f)

        return redirect(url_for('login'))

    return render_template('register.html')

# Route für Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user_file = os.path.join(users_folder, f"{email}.json")
        if os.path.exists(user_file): # Prüft ob Benutzerdatei existiert
            with open(user_file, 'r') as f:
                user_data = json.load(f)

            if check_password_hash(user_data['password'], password): # Prüft das Passwort 
                session['user'] = email # Speichert Benutzer in Session
                return redirect(url_for('dashboard'))

    return render_template('login.html')

# Route für Logout
@app.route('/logout')
def logout():
    session.pop('user', None) # Entfernt User aus Session
    return redirect(url_for('index'))

# Route für dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' not in session: # Falls User nicht eingeloggt, Weiterleitung zum Login
        return redirect(url_for('login'))

    user_file = os.path.join(users_folder, f"{session['user']}.json")
    with open(user_file, 'r') as f:
        user_data = json.load(f)

    # Sortiert Aktivitäten nach User Auswahl (somit kann User selbst entscheiden, wie er die Aktivitäten sortieren möchte, nicht alle User haben die gleichen Bedürfnisse) 
    sort_by = request.args.get('sort_by', 'date')
    sort_order = request.args.get('sort_order', 'desc')

    if sort_by == 'type':
        activities = sorted(user_data['activities'], key=lambda x: x['type'])
    elif sort_by == 'distance':
        activities = sorted(user_data['activities'], key=lambda x: float(x.get('distance', 0)), reverse=(sort_order == 'desc'))
    elif sort_by == 'elevation':
        activities = sorted(user_data['activities'], key=lambda x: float(x.get('elevation', 0)), reverse=(sort_order == 'desc'))
    elif sort_by == 'duration':
        activities = sorted(user_data['activities'], key=lambda x: float(x.get('duration', 0)), reverse=(sort_order == 'desc'))
    else:
        activities = sorted(user_data['activities'], key=lambda x: x['date'], reverse=(sort_order == 'desc'))
    
    # Sammelt alle Aktivitäten der aktuellen Woche (notwendig für wöchentliches Ziel)
    start_of_week = get_start_of_week()
    end_of_week = get_end_of_week()
    weekly_activities = [
        activity for activity in activities 
        if start_of_week <= datetime.strptime(activity['date'], '%Y-%m-%d') <= end_of_week
    ]

    # Berechnet den Fortschritt des wöchentlichen Ziels (im Ausdauersportbereich ist es üblich, dass Ziele wöchentlich gesetzt werden, um die Leistung zu steigern)
    weekly_total = 0
    if user_data['weekly_goal']['type'] == 'distance':
        weekly_total = sum(float(activity['distance']) for activity in weekly_activities if activity['distance'])
    elif user_data['weekly_goal']['type'] == 'time':
        weekly_total = sum(float(activity['duration']) for activity in weekly_activities if activity['duration'])

    goal_value = user_data['weekly_goal']['value']
    if goal_value > 0:
        progress_percentage = min((weekly_total / goal_value) * 100, 100)
    else:
        progress_percentage = 0

    return render_template('dashboard.html', activities=activities, progress_percentage=progress_percentage, sort_by=sort_by, sort_order=sort_order)

# Funktion um Wochenstart zu definieren
def get_start_of_week():
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday()) 
    return start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)

# Funktion um Wochenende zu definieren
def get_end_of_week():
    start_of_week = get_start_of_week()
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)
    return end_of_week

# Flask-Kontextprozessor, damit Enumerate in Vorlage verwendet werden kann
@app.context_processor
def utility_processor():
    return dict(enumerate=enumerate)

# Route um Aktivitäten hinzuzufügen 
@app.route('/add_activity', methods=['GET', 'POST'])
def add_activity():
    if 'user' not in session: # Falls User nicht eingeloggt, Weiterleitung zum Login
        return redirect(url_for('login'))

    if request.method == 'POST':
        activity_id = str(uuid.uuid4())  # Erstellt eine eindeutige ID für die jewielige Aktivität. 4 ist komlett random, 1 würde auch gehen (basiert auf Hostname und Zeit)
        activity_type = request.form['activity_type']
        distance = request.form['distance']
        elevation = request.form['elevation'] if request.form['elevation'] else 0
        duration = request.form['duration']
        date = request.form['date']

        # Erstellen einer neuen Aktivität (Es wurden diese Daten gewähö, da sie für die meisten Aktivitäten relevant sind. Sollten User zukünftig weitere Daten wünschen, können diese hinzugefügt werden)
        new_activity = {
            'id': activity_id,
            'type': activity_type,
            'distance': distance,
            'elevation': elevation,
            'duration': duration,
            'date': date
        }

        user_file = os.path.join(users_folder, f"{session['user']}.json")
        with open(user_file, 'r') as f:
            user_data = json.load(f)

        user_data['activities'].append(new_activity) # Fügt neue Aktivität dem User hinzu

        with open(user_file, 'w') as f:
            json.dump(user_data, f)

        return redirect(url_for('dashboard'))

    return render_template('add_activity.html')

# Route zur Zielsetzung 
@app.route('/set_goal', methods=['GET', 'POST'])
def set_goal():
    if 'user' not in session: # Falls User nicht eingeloggt, Weiterleitung zum Login
        return redirect(url_for('login'))

    user_file = os.path.join(users_folder, f"{session['user']}.json")
    with open(user_file, 'r') as f:
        user_data = json.load(f)

    current_goal = user_data.get('weekly_goal', {'type': None, 'value': 0})

    # Setzt wöchentliches Ziel (User kann selbst entscheiden, ob er Distanz oder Zeit als Ziel setzen möchte. Höhenmeter kann nicht gewählt werden, da keine Pflichteingabe. Gerade im Laufsport haben Höhenmeter keine zentrale Relevanz)
    if request.method == 'POST':
        goal_type = request.form['goal_type']
        goal_value = request.form['goal_value']

        user_data['weekly_goal'] = {
            'type': goal_type,
            'value': float(goal_value)
        }

        with open(user_file, 'w') as f:
            json.dump(user_data, f)

        return redirect(url_for('dashboard'))

    return render_template('set_goal.html', current_goal=current_goal)

# Route Aktivität löschen
@app.route('/delete_activity/<activity_id>', methods=['POST'])
def delete_activity(activity_id):
    if 'user' not in session: # Falls User nicht eingeloggt, Weiterleitung zum Login
        return redirect(url_for('login'))

    # Laden der JSON-Datei
    user_file = os.path.join(users_folder, f"{session['user']}.json")
    with open(user_file, 'r') as f:
        user_data = json.load(f)

    # Entfernen der Aktivität mit der eindeutigen Aktivitäts-ID (Falls Aktivität nicht korrekt hinzugefügt wurde, kann sie so auch wieder entfernt werden)
    activities = user_data['activities']
    updated_activities = [activity for activity in activities if activity['id'] != activity_id]

    # Aktualisieren der JSON-Datei
    user_data['activities'] = updated_activities
    with open(user_file, 'w') as f:
            json.dump(user_data, f)

    return redirect(url_for('dashboard'))

# Einbindung Impressum
@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

# Einbindung Datenschutz
@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

if __name__ == '__main__': # Prüft ob als Hauptprogramm ausgeführt werden soll
    app.run(debug=True, port=5005) # Aktiviert Debug-Modus & setzt Port fest 


