from flask import render_template,request,redirect,session

def mainPage(app):
    @app.route('/')
    def home():
        return render_template("index.html")