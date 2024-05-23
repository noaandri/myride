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
#testtest

if __name__ == '__main__':
    app.run(debug=True, port=3000)
