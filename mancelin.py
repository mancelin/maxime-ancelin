# -*- coding: utf-8 -*-


from flask import Flask, render_template
import pymongo


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

#@app.route("/add_project")
@app.route("/add")
def add_project():
    db.projets.save( { 'name' : "mongo" } , safe=True)
    print "add !"
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html', title=' - Contact')

@app.route("/CV")
def cv():
    return render_template('CV.html', title=' - CV')

@app.route("/projets")
def projets():
    return render_template('projets.html', title=' - Projets')


@app.route("/sites_amis")
def sites_amis():
    return render_template('sites_amis.html', title=' - Site amis')


if __name__ == "__main__":
    app.run()
