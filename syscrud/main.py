from Entity.Pessoa import Pessoa

while True:
        print("\nLista de produtos:")
        print("1. Cadastro de usuário")
        print("2. Listagem de usuário")
        print("3. Fazer consulta de usuário por ID")
        print("4. Fazer atualização de usuário")
        print("5. Apagar usuário")
        print("6. Log out")
 
        opc = input("Escolha umas das opção a seguir: ")
 
        if opc == "1":
            nome = input("Qual o nome: ")
            cpf = input("Digite o cpf: ")
            email = input("Qual o email: ")
            telefone = input("Qual o telefone: ")
            endereco = input("Qual o endereço: ")
            cidade = input("Qual a cidade: ")
            pessoa = (nome,cpf,email,telefone,endereco,cidade)
            pessoa = Pessoa()
            pessoa.cadastrar()
 
        elif opc == "2":
            produtos = db.select_all_products()
            print("\nListando os produtos...:")
            for produto in produtos:
                print(produto)
 
        elif opc == "3":
            product_id = int(input("Digite qual é o ID do produto: "))
            produto = db.select_product_by_id(product_id)
            print("\nAqui estao os detalhes do produto:")
            print(produto)
 
        elif opc == "4":
            product_id = int(input("Qual é o ID do produto que deseja atualizar: "))
            nome = input("Qual é o novo nome do produto: ")
            descr = input("Digite qual é a nova descrição: ")
            valor = float(input("Digite qual é o novo preço: "))
            qtd = int(input("Digite qual é a nova quantidade: "))
            db.update_product(product_id, nome, descr, valor, qtd)
 
        elif opc == "5":
            product_id = int(input("Qual seria o ID do produto que deseja excluir: "))
            db.delete_product(product_id)
 
        elif opc == "6":
            print("Log out...")
            break
 
        else:
            print("Essa opção não é valida tente novamente.")