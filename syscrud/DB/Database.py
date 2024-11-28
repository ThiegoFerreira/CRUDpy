import mysql.connector

class Database():
    def __init__(self,banco = 'sistema_crud'):
        self.banco = banco
    
    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database=self.banco, user = 'root', password ='')
        
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com sucesso!",db_info)
        else:
            print("Error")

    def insert_client(self,param):
        self.connect()
        try:

            self.cursor.execute ("INSERT INTO pessoa (nome,cpf,email,fone,endereco,cidade) VALUES (%s,%s,%s,%s,%s,%s)",param)
            self.conn.commit()
            print("Cadastrado com sucesso.")

        except Exception as error:
            print(error)

    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM pessoa;")
            cliente = self.cursor.fetchall()
            for cli in cliente:
                print(cli)

        except Exception as error:
            print(error)
    
    def select_client_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM pessoa WHERE id = {id};")
            cliente = self.cursor.fetchone()
            return cliente

        except Exception as error:
            print(error)

    def update_client(self,id):
        self.connect()
        try:
            cli = list(self.select_client_by_id(id))
            cli[1] = input("Digite o novo nome:")
            cli[2] = input("Digite o novo cpf:")
            cli[3] = input("Digite o novo email:")
            cli[4] = input("Digite o novo fone:")
            cli[5] = input("Digite o novo endereco:")
            cli[6] = input("Digite o novo cidade:")

            self.cursor.execute(f"UPDATE pessoa SET nome = '{cli[1]}', cpf = '{cli[2]}', email = '{cli[3]}',fone = '{cli[4]}', endereco ='{cli[5]}', cidade = '{cli[6]}'  WHERE id = {cli[0]}")
            self.conn.commit()
            print("Cliente atualizado com sucesso")
            # self.select_client_by_id(cli[0])

        
                   
        except Exception as error:
            print(error)

    def delete_client(self,id):
        self.connect()

        try:
            self.cursor.execute(f"DELETE FROM pessoa WHERE id = {id}")
            self.conn.commit()
            print("Cliente deletado com sucesso!")
            self.select_client()

        except Exception as error:
            print(error)

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada!")

    # ____________________________________________________________________________________________________________________
            
    def insert_produto(self):
        self.connect()
        try:
            args = ("ProdutoZ", "Marca Z","Modelo Hyper", "Uma máquina muito louca", 199.00, "Eletrônico", 20, 5.00)
            self.cursor.execute ("INSERT INTO produto (nome,marca,modelo,descricao,preco,tipo,tamanho,peso) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",args)
            self.conn.commit()
            print ("Produto cadastrado com sucesso")
        except Exception as error:
            print(error)
    
    def select_produto(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM produto")
            produto = self.cursor.fetchall()
            for prod in produto:
                print(prod)

        except Exception as error:
            print(error)

    def select_produto_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM produto WHERE id = {id}")
            produto = self.cursor.fetchone()
            return produto
        except Exception as error:
            print(error)

    def update_produto(self,id):
        self.connect()
        try:
            prod = list(self.select_produto_by_id(id))
            prod[1] = input("Digite o novo nome:")
            prod[2] = input("Digite a nova marca:")
            prod[3] = input("Digite o novo modelo:")
            prod[4] = input("Digite a nova descricao:")
            prod[5] = input("Digite o novo preço:")
            prod[6] = input("Digite o novo tipo:")
            prod[7] = input("Digite o novo tamanho:")
            prod[8] = input("Digite o novo peso:")

            self.cursor.execute(f"UPDATE produto SET nome = '{prod[1]}', marca = '{prod[2]}', modelo = '{prod[3]}',descricao = '{prod[4]}', preco ={prod[5]}, tipo = '{prod[6]}', tamanho = '{prod[7]}', peso = {prod[8]}  WHERE id = {prod[0]}")
            self.conn.commit()
            print("Produto atualizado com sucesso")
            # conf = self.select_client_by_id(prod[0])
            # print(conf)
                  
        except Exception as error:
            print(error)

    def delete_produto(self,id):
        self.connect()

        try:
            self.cursor.execute(f"DELETE FROM produto WHERE id = {id}")
            self.conn.commit()
            print("Produto deletado com sucesso!")
            self.select_produto()

        except Exception as error:
            print(error)

if __name__ == "__main__":
    db = Database()
    db.connect()
    # db.insert_client()
    # db.select_client()
    # db.select_client_by_id(2)
    # db.delete_client(3)
    # db.update_client(5)
    # db.insert_produto()
    # db.select_produto()
    # db.select_produto_by_id(2)
    # db.update_produto(2)
    # db.delete_produto(1)
    # db.close_connection()