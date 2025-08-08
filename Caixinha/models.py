import sqlite3

def init_db():
    try:
        with sqlite3.connect("Banco.db") as conexao:
            cur = conexao.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    senha TEXT NOT NULL
                )
            ''')

            cur.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    descricao TEXT,
                    qnt_disponivel INTEGER NOT NULL,
                    valor REAL NOT NULL
                )
            ''')

            cur.execute('''
                CREATE TABLE IF NOT EXISTS compras (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    
                    produto_id INTEGER NOT NULL,
                    qnt_comprada INTEGER NOT NULL,
                    valor_total REAL NOT NULL,
                    FOREIGN KEY(produto_id) REFERENCES produtos(id)
           
                )
            ''')

            conexao.commit()
            print("Banco de dados inicializado com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
