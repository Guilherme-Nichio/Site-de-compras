from flask import Flask,render_template
from models import init_db
init_db()
app = Flask(__name__)
from routes.main import mainPage
mainPage(app)


if __name__ == '__main__':
    app.run(debug=True)