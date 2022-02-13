from connectDatabase import Database

class Pessoa:
    def __init__(self):
        self.db = Database()
    
    def todosUsuarios(self):
        data = self.db.exibePessoas()
        # print(data)
        return data

    def inserirUsuario(self):
        print('usuário inserido!')
    
    def removeUsuario(self):
        print('Remove usuário!')


p = Pessoa()
p.todosUsuarios()
p.inserirUsuario()
p.removeUsuario()