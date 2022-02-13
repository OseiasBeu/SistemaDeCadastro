import sqlite3

conn = sqlite3.connect(r'C:\Users\f48014593820\Documents\Python Scripts\Projects\SistemaDeCadastro\database\sistemacadastro.db')
cursor = conn.cursor()

#Criação da tabela:
cursor.execute("""
CREATE TABLE pessoas(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
);
""")

print('Tabela Criada com sucesso!')

# Inserção de registros=
cursor.execute("""
INSERT INTO pessoas (nome,email) VALUES ('Cristian','cristian@gmail.com')
""")

conn.commit()

#Consulta a tabela
cursor.execute(
    """
    SELECT * FROM pessoas;
    """
)

for linha in cursor.fetchall():
    print(linha)

conn.close()
