pip install Flask   
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name="Noa Roth"
    return render_template("index.html", name=name)

@app.route('/page1')
def hi():
    name="Page1"
    return render_template("Page1.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
