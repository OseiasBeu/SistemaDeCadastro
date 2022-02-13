from distutils.util import execute
import sqlite3
import pandas as pd


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(r'database\sistemacadastro.db')
        self.cursor = self.conn.cursor()

    def exibePessoas(self):
        df = pd.read_sql_query('SELECT * FROM pessoas;', self.conn)
        pessoas = df
        # print(pessoas)
        return pessoas.values

    def buscaPessoaPorNome(self, nome):
        query = f'SELECT * FROM pessoas WHERE nome LIKE "%{nome}%"'
        df = pd.read_sql_query(query, self.conn)
        return df.values

    def buscaPessoaPorId(self, id):
        query = f'SELECT * FROM pessoas WHERE id ={id}'
        df = pd.read_sql_query(query, self.conn)
        return df.values
    
    def inserirPessoa(self,nome,email):
        lista = [nome,email]
        self.cursor.execute('INSERT INTO pessoas (nome,email) VALUES (?,?)',lista)
        self.conn.commit()
        return 'Registro inserido com sucesso!'

    def inserirLote(self,caminho):
        wb = pd.read_csv(caminho)
        df = pd.DataFrame(wb)

        for i, row in df.iterrows():
            # print(row[0].split(';')[0])
            query = f"INSERT INTO pessoas (nome,email) VALUES ('{row[0].split(';')[0]}','{row[0].split(';')[1]}')"
            # print(query)
            self.cursor.execute(query)
        self.conn.commit()
        
    def removeUsuarioPorNome(self,nome):
        self.cursor.execute(f'DELETE FROM pessoas WHERE nome LIKE "%{nome}%"')
        self.conn.commit()
        return 'Registro apagado com sucesso!'
    
    def removeUsuarioPorId(self,id):
        lista = [int(id)]
        self.cursor.execute('DELETE FROM pessoas WHERE id =?',lista)
        self.conn.commit()
        return 'Registro apagado com sucesso!'

# db = Database()
# db.inserirLote(r'C:\Users\f48014593820\Documents\Python Scripts\Projects\SistemaDeCadastro\ListaDeContatosEmLote.CSV')