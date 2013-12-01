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
    return render_template('CV.html', title=' - CV')

@app.route("/projets")
def projets():
    return render_template('projets.html', title=' - Projets')

@app.route("/contact")
def contact():
    return render_template('contact.html', title=' - Contact')

@app.route("/sites_amis")
def sites_amis():
    return render_template('sites_amis.html', title=' - Site amis')


if __name__ == "__main__":
    app.run()
