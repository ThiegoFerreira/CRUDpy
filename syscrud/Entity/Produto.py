from DB.Database import Database

class Produto():
    def __init__(self) -> None:
        self.nome = None
        self.marca= None
        self.modelo= None
        self.descricao= None
        self.preco= None
        self.tipo= None
        self.tamanho= None
        self.peso= None
        self.banco = Database()

    def cadastrarProduto(self):
        tupla = (self.nome,self.marca,self.modelo,self.descricao,self.preco,self.tipo,self.tamanho,self.peso)
        res =  self.banco.insert_product(tupla)
        return res
    
    def selecionar(self):
        dados = self.banco.select_client()
        return dados
        
    def selecionar_por_id(self,id):
        dado = self.banco.select_client_by_id(id)
        return list(dado)
        
    def atualizar(self,lista):
        res = self.banco.update_client(lista)
        return res
        
    def deletar(self,id):
        res = self.banco.delete_client(id)
        return res