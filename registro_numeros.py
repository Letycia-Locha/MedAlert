import sqlite3
from datetime import datetime

# Inicializa o banco de dados
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Cria a tabela para medicações com todas as colunas necessárias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            horarios TEXT NOT NULL,
            duracao TEXT NOT NULL,
            data_inicio TEXT NOT NULL,
            responsavel TEXT NOT NULL
        )
    ''')

    # Cria a tabela para armazenar o número de telefone
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Insere ou atualiza o número de telefone do usuário
def register_phone_number(phone_number):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM user')  # Remove registros antigos
    cursor.execute('INSERT INTO user (phone_number) VALUES (?)', (phone_number,))
    conn.commit()
    conn.close()

# Insere uma nova medicação
def register_medication(name, horarios, duracao, responsavel):
    data_inicio = datetime.now().strftime('%Y-%m-%d')  # Data atual no formato YYYY-MM-DD
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO medications (name, horarios, duracao, data_inicio, responsavel) VALUES (?, ?, ?, ?, ?)',
        (name, horarios, duracao, data_inicio, responsavel)
    )
    conn.commit()
    conn.close()

# Recupera os dados cadastrados
def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user')
    user = cursor.fetchone()
    cursor.execute('SELECT * FROM medications')
    medications = cursor.fetchall()
    conn.close()
    return user, medications

# Desativa alertas para uma medicação específica
def remove_medication(name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM medications WHERE name = ?', (name,))
    conn.commit()
    conn.close()

# Depuração do banco de dados
def debug_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    print("\nDEBUG: Dados na tabela medications:")
    cursor.execute("SELECT * FROM medications")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()
