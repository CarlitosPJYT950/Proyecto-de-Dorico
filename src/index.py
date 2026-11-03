import sqlite3

conexao = sqlite3.connect("coin.sql")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
cursor.execute("INSERT INTO usuarios (nome) VALUES ('Juan')")

conexao.commit()

cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())