# -*- coding: utf-8 -*-


from flask import Flask, render_template


# configuration
DEBUG = True

# create application
app = Flask(__name__)
app.config.from_pyfile('./config.ini', silent=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/CV")
def cv():
    return render_template('CV.html')

@app.route("/projets")
def projets():
    return render_template('projets.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/sites_amis")
def sites_amis():
    return render_template('sites_amis.html')


if __name__ == "__main__":
    app.run()
