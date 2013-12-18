# -*- coding: utf-8 -*-


from flask import Flask, render_template
import pymongo

from controllers import projects


# configuration db
db_host_name = 'localhost'
db_port = 27017
db_name = 'mancelin'

# create application
app = Flask(__name__)
app.config.from_pyfile('./config.ini', silent=True)
db = pymongo.Connection(host=db_host_name, port=db_port)[db_name]


# routes
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ADMIN")
def admin():
    return projects.admin(db)

@app.route("/contact")
def contact():
    return render_template('contact.html', title=' - Contact')

@app.route("/CV")
def cv():
    return render_template('CV.html', title=' - CV')

@app.route("/logout")
def logout():
    # logout
    return render_template('index.html')

@app.route("/projets")
def projets():
    return projects.list(db)


@app.route("/sites_amis")
def sites_amis():
    return render_template('sites_amis.html', title=' - Site amis')


if __name__ == "__main__":
    app.run()
