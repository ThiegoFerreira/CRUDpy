import mysql.connector

class Database():
    def __init__(self,banco = 'sistema_crud'):
        self.banco = banco
    
    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database=self.banco,user='root',password='')
        
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("CONECTADO COM SUCESSO!!!!",db_info)
        else:
            print("ERROR")

    def insert_client(self,param:tuple):
        self.connect()
        try:
            self.cursor.execute(""" 
                                INSERT INTO pessoa 
                                (nome,cpf,email,fone,endereco,cidade) 
                                VALUES (%s,%s,%s,%s,%s,%s)
                                """,param)
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

        finally:
            self.close_connection()
    def insert_product(self,param:tuple):
        self.connect()
        try:
            self.cursor.execute(""" 
                                INSERT INTO produto 
                                (nome,marca,modelo,descricao,preco,tipo,tamanho,peso) 
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                                """,param)
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

        finally:
            self.close_connection()

    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM pessoa;")
            clientes = self.cursor.fetchall()
            
            return clientes

        except Exception as error:
            print(error)

        finally:
            self.close_connection()
    def select_product(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM produto;")
            produtos = self.cursor.fetchall()
            
            return produtos

        except Exception as error:
            print(error)

        finally:
            self.close_connection()

    def select_client_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM pessoa WHERE id = {id};")
            cliente = self.cursor.fetchone()
            return cliente

        except Exception as error:
            print(error)

        finally:
            self.close_connection()

    def update_client(self,lista):
        self.connect()
        try:

            self.cursor.execute(f"""
                                UPDATE pessoa 
                                SET nome = '{lista[1]}',
                                cpf = '{lista[2]}',
                                email = '{lista[3]}',
                                fone = '{lista[4]}',
                                endereco = '{lista[5]}',
                                cidade = '{lista[6]}'
                                WHERE id = {lista[0]}
                                """)
            self.conn.commit()
            return True
            
        except Exception as error:
            print(error)

        finally:
            self.close_connection()

    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM pessoa WHERE id = {id}")
            self.conn.commit()
            return True
            

        except Exception as error:
            print(error)
        
        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!")

if __name__ == "__main__":
    db = Database()