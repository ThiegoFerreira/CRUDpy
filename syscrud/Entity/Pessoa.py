from DB.Database import Database

class Pessoa():
    def __init__ (self)->None:
        self.nome = None
        self.cpf = None
        self.email = None
        self.fone = None
        self.endereco= None
        self.cidade = None
    
    def cadastrar(self):
        tupla = (self.nome,self.cpf,self.email,self.fone,self.endereco,self.cidade)
        bd= Database()
        bd.insert_client(tupla)

    def listarPessoa(self):
        db = Database()
        pessoas = db.select_client()
        return pessoas
