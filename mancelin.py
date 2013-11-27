# -*- coding: utf-8 -*-


from flask import Flask


# configuration
DEBUG = True

# create application
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return "Page d'acceuil"

if __name__ == "__main__":
    app.run()
