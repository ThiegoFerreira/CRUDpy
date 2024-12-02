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
    
    def selecionarProduto(self):
        dados = self.banco.select_product()
        return dados
        
    def selecionarProduto_por_id(self,id):
        dado = self.banco.select_product_by_id(id)
        return list(dado)
        
    def atualizarProduto(self,lista):
        res = self.banco.update_product(lista)
        return res
        
    def deletarProduto(self,id):
        res = self.banco.delete_product(id)
        return res