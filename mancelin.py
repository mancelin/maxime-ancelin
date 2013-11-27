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

if __name__ == "__main__":
    app.run()
