from flask import Flask, escape, url_for, render_template
app = Flask(__name__)

@app.route('/')
def html():
    return render_template('home.html')