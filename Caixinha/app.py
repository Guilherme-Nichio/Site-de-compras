from flask import Flask,render_template

app = Flask(__name__)
from routes.main import mainPage
mainPage(app)


if __name__ == '__main__':
    app.run(debug=True)