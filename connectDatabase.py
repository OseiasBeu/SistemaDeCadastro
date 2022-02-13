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
