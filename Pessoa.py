from connectDatabase import Database

class Pessoa:
    def __init__(self):
        self.db = Database()
    
    def todosUsuarios(self):
        data = self.db.exibePessoas()
        # print(data)
        return data

    def buscaPessoaPorNome(self,nome):
        data = self.db.buscaPessoaPorNome(nome)
        return data

    def buscaPessoaPorId(self,id):
        data = self.db.buscaPessoaPorId(id)
        return data

        
    def inserirPessoa(self,nome,email):
        data = self.db.inserirPessoa(nome,email)
        return data

    def inserirLote(self,caminho):
        data = self.db.inserirLote(caminho)
        return data

    
    def removeUsuarioPorNome(self,nome):
        data = self.db.removeUsuarioPorNome(nome)
        return data

    def removeUsuarioPorId(self,id):
        data = self.db.removeUsuarioPorId(id)
        return data


# p = Pessoa()
# p.todosUsuarios()
# p.buscaPessoaPorNome('Cristian')