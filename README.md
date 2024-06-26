### Setup für Programm User:
<ol>
    <li>Um das Programm zu starten, muss der User lokal eine Datei "config.py" erstellen und darin einen secret_key definieren (Kann ein beliebiger key sein). Dieser wird aus sicherheitsgründen nicht mitgegeben. Ebenfalls muss ein Ordner "users" erstellt werden, in welchem alle userdaten gespeichert werden. </li>
    <li>Der User muss sich nun registrieren und seine Daten werden in seinem User File gespeichert.</li>
    <li>Nun kann sich der User einloggen und kann über die Funktion "Neue Aktivität" Aktivitäten hinzufügen. Diese bekommt er im Dashbaord angezeigt. Hat er eine Aktitvät zu viel oder falsch erfasst, kann er diese auch über das dashboard löschen. Ebenfalls kanne er alle erfassten Aktivitäten nach belieben sortieren.</li>
    <li>Über die Funktion "Wöchentliches Ziel setzen" kann der User ein wöchentliches Distanz- oder Zeitziel definieren. Sollte er bereits eines erfasst haben, kann er einfach ein neues erfassen und das alte ist überschrieben. Den aktuellen Fortschritt des wöchentlichen Zieles wird dem User ebenfalls auf den Dashbaord angezeigt.</li>
    <li>Sollte der User Kontakt zum Seitenbetreiber aufnehmen wollen, kann er dies über die Kontaktdaten im Impressum tun. Auch die Datenschutzrichtlinien erreicht er per Link im Footer.</li>
</ol>

# myride

## Ausgangslage 

#### Soll: 

Meine Applikation soll begeisterten Radfahrern eine übersichtliche Möglichkeit bieten, gefahrene KM sowie Höhenmeter zu tracken sowie neue Rides zu planen. Zudem wird aufrgrund der absolvierten Fahrten der Fortschritt getrackt. Es können persönliche Ziele definiert werden und so Routen und Trainings spezifisch auf diese Ziele geplant werden.

#### Ist: 

Mit myride können Ausdauersportler (Radfahren & Laufen) ihre Aktivitäten erfassen. Erfasst werden können die Metriken Distanz, Höhenmeter, Zwie sowie das Datum der Aktivität. Anhand diesen Kriterin kann durch alle erfassten Ereignisse auch gefiltert werden. Als ergänzende Funktion können wöchentliche Ziele definiert werden. Hierbei kann zwischen einem Distanz- sowie Zeitziel ausgewählt werden. Die Aktivitäten innerhalb einer Woche werden per datetime-Modul zusammengerechnet und somit wird der prozentuale Fortschritt im Dashboard angegeben. 

## Projektideen / Funktion - was kann man mit Ihrer Software machen und welches Problem wird gelöst

#### Soll: 

Die App soll eine ganz simple und all in one Lösung für Radfahrer bieten. Der Nutzer kann die gefahrenen Kilometer und Höhenmeter ganz simpel eintragen. Dies gilt als grundlegende Daten welche dann veranschaulicht werden. 

#### Ist:

Die App bietet eine ganz simple Lösung Aktivitäten im Rad- und Laufsport zusammen zufassen. Zudem kann man individuelle Ziele definieren und deren Fortschtschritt tracken. 


## Beschreibung, welche verschiedenen Ansichten es gibt (4-8 sind sinnvoll)

#### Soll: 

<ul>
    <li>Startseite - Übersichtsseite mit einer groben Übersicht an gefahrenen Kilometer und Höhenmeter sowie die aktuellen Ziele</li>
    <li>Tracking - Hier werden die gefahrenen KM & HM eingetragen und somit die gefahrenen Rides getrackt</li>
    <li>Ziele - Hier werden Ziele definiert und der Fortschritt der Ziele gemessen</li>
    <li>Planing - Hier können passende Rides geplant werden, welche auf das aktuelle Ziel einzahlen</li>
    <li>Kalender - Hier kann man sehen an welchen Tagen ein Training absolviert wurde, und wie viel gefahren wurde</li>
</ul>

#### Ist:

<ul>
    <li>Login - Login Funktion</li>
    <li>Registrierung - Registrations Funktion</li>
    <li>Dashboard - Übersicht über erledigte Aktivitäten / Möglichkeit zur Sortierung deren / aktueller Fortschritt</li>
    <li>Aktivität hinzufügen - Aktivitäten erfassen</li>
    <li>Ziel setzen - Möglichkeit ein wöchentliches Ziel zu setzen</li>
    <li>Impressum - Seitenbetreiber & Kontaktdaten</li>
    <li>Datenschutz - Datenschutzrichtlinien (generiert durch ChatGPT)</li>
</ul>

## Beschreibung, welche Daten Sie einlesen, speichern oder ausgeben

#### Soll: 

Die Daten werden von den Usern direkt selber eingegeben und gespeichert
(Optional kann geprüft werden, ob eien alfälliges einlesen über Garmin / Strava / Apple Fitness / etc. möglich ist)
Es werden jedem User seine eigenen Daten ausgegeben welche er auch eingegeben hat. Diese können jedoch summiert oder gezielt eingegeben werden.

#### Ist:

Die User geben ihre Daten selber ein. Sie können Distanz, Zeit, Höhenmeter und das Datum eingeben. Eine API wurde bewusst verzichtet.

## Beschreibung, welche Funktionen der Nutzer auslösen kann

#### Soll:

<ul>
    <li>Tracking - Der User kann Daten eingeben und anpassen</li>
    <li>Ziele definieren - Der User kann Ziele definieren (KM & HM), welche ihm dann als definierte Ziele ausgegeben werden und worauf die nächsten Trainings einzahlen.</li>
    <li>Planing - Der User kann in der App Planungen vornehmen</li>
</ul>

#### Ist:

<ul>
    <li>Registrierung - der User kann isch registrieren</li>
    <li>Login - der User kann sich einloggen</li>
    <li>Aktivität hinzufügen - der User kann Rad & Lauf Aktivitäten hinzufügen</li>
    <li>Aktivitäten sortieren - der User kann die Aktivitäten nach verschiednene Kriterien sortieren</li>
    <li>Ziel setzen - der User kann ein Distanz oder Zeit Ziel setzen um den Fortschritt zu messen</li>
</ul>

## Überlegunen bei der Entstehung


## Probleme & Herausforderungen

Während der Erarbeitung haben sich mir diverse Herausforderungen gestellt. Diese werde ich hier erläutern und wie ich sie gelöst habe.

<ul>
    <li>Löschen einer Aktivität: Beim ersten Versuch die Löschfunktion zu integrieren habt es beim Löschen die Aktivität jeweils nach Index gelöscht. Nach einiger Recherche bin ich auf die Variante mit dem uuid Verfahren gekommen. Ich habe mich für Variante 4 entschieden, welche jeder Aktivität eine eindeutige ID gibt und beim Löschen diese auch wieder entfernt.</li>
    <li>Das Definieren des Wochenstarts, sowie des Wochenende hat sich als schwieriger herausgestellt als gedacht. Mit der Funktion datetime wird nun ausgerechnet, welche Aktivitäten in der aktuellen Woche stattgefunden haben, damit das wöchentliche Ziel berechnet wird.</li>
    <li>Die Buttons zum Löschen einer Aktivität aus der Liste haben wie man sehen kann einen unschönen Rand. Diesen zu entfernen ist mir nicht gelungen. Die Verzweiflung ist gross geworden aber ich musste akzeptieren, dass meine Fähigkeiten wohl nicht genügen, dies zu richten.</li>
</ul>

## Quellen

Folgende Quellen dienten zur Erarbeitung des Projekts:
* Ingmar Beatge und die Vorlesungsunterlagen zu PROG2
* Vorlesungsfolien PROG1 (Autor: Fabian Odoni)
* [Stackoverflow](https://stackoverflow.com/)
* [Github-Copilot](https://github.com/features/copilot)
* [Chat GPT](https://chatgpt.com/)
* [Flask-Dokumentation](https://flask.palletsprojects.com/en/3.0.x/) 
* Untestützung eines Arbeitskollegen (gelernter Informatiker)
* Danke Lukas fürs merhmalige troubleshooten!




