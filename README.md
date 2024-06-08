### Setup für Programm User:
<ul>
    <li>Bei app.py Line 8 (app.secret_key = secret_key) secret_key in config.py erstellt werden muss um Sessions anzulegen. Für den secret_key kann eine beliebige Zeichenfolge gesetzt werden.</li>
</ul>

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



## Probleme & Herausforderungen

Während der Erarbeitung haben sich mir diverse Herausforderungen gestellt. Diese werde ich hier erläutern und wie ich sie gelöst habe.

<ul>
    <li>Löschen einer Aktivität: Beim ersten Versuch die Löschfunktion zu integrieren habt es beim Löschen die Aktivität jeweils nach Index gelöscht. Nach einiger Recherche bin ich auf die Variante mit dem uuid Verfahren gekommen. Ich habe mich für Variante 4 entschieden, welche jeder Aktivität eine eindeutige ID gibt und beim Löschen diese auch wieder entfernt.</li>
    <li> </li>


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




