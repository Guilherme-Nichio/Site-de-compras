from flask import render_template,request,redirect,session
import sqlite3

def init_db():
    try:
        with sqlite3.connect("Banco.db") as conexao:
            cur = conexao.cursor()
            cur.execute('''
                INSERT INTO usuarios (nome, senha) values('gui','123') 
                        ''')
            conexao.commit()
            print("INSERIDO.")

    except sqlite3.Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
        
init_db()
def mainPage(app):
    @app.route('/', methods=['GET', 'POST'])

    def home():
        if request.method == 'POST':

            user = request.form['User']
            senha = request.form['Senha' ]


        return render_template("login.html")