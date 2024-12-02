from Entity.Cliente import Cliente
from Entity.Produto import Produto

while True:

    opcao = input("Digite (1) para cliente, digite (2) produtos ou digite (3) para sair: ")

    if opcao == "1":

        print("1. Cadastro de usuário")
        print("2. Listagem de usuário")
        print("3. Fazer consulta de usuário por ID")
        print("4. Fazer atualização de usuário")
        print("5. Apagar usuário")
        print("6. Sair")

        opcao2 = input("Digite qual opção: ")
        if opcao2 == "1":
            
            cli1 = Cliente()

            cli1.nome = input("Digite o nome: ")
            cli1.cpf = input("Digite o cpf: ")
            cli1.email = input("Digite o email: ")
            cli1.fone = input("Digite o fone: ")
            cli1.endereco = input("Digite o endereco: ")
            cli1.cidade = input("Digite o cidade: ")

            result = cli1.cadastrar()
            if result == True:
                print("Cadastrado com Sucesso!!!")

        elif opcao2 == "2":
            cli1 = Cliente()

            dados_do_banco = cli1.selecionar()

            for cliente in dados_do_banco:
                print(f"id: {cliente[0]} nome: {cliente[1]} login: {cliente[2]}")


        elif opcao2 == "3":
            cli1 = Cliente()

            cli = int(input("Digite o id a consultar: "))

            pessoa = cli1.selecionar_por_id(cli)

            print(pessoa)

            
        elif opcao2 == "4":

            id_cli = int(input("Digite o id: "))

            cliente_selecionado = cli1.selecionar_por_id(id_cli)

            cliente_selecionado[1] = input("DIGITE O NOVO NOME: ")
            cliente_selecionado[2] = input("DIGITE O NOVO CPF: ")
            cliente_selecionado[3] = input("DIGITE O NOVO EMAIL: ")
            cliente_selecionado[4] = input("DIGITE O NOVO FONE: ")
            cliente_selecionado[5] = input("DIGITE O NOVO ENDERECO: ")
            cliente_selecionado[6] = input("DIGITE O NOVO CIDADE: ")

            atualizacao = cli1.atualizar(cliente_selecionado)
            if atualizacao == True:
                print("Cliente atualizado com sucesso!!!")
                cli_atualizado = cli1.selecionar_por_id(cliente_selecionado[0])
                print(cli_atualizado)

        elif opcao2 == "5":
            id_cli = int(input("Digite o ID: "))

            cli_deletado = cli1.deletar(id_cli)
            if cli_deletado == True:
                print("Deletado com sucesso!")
                dados_do_banco = cli1.selecionar()

                for cliente in dados_do_banco:
                    print(f"id: {cliente[0]} nome: {cliente[1]} login: {cliente[2]}")

        elif opcao2 == "6":
            print ("Saindo")
            continue

        else:
            print("Opção inválida.")

    elif opcao == "2":
        print("1. Cadastro de produtos")
        print("2. Listagem de produtos")
        print("3. Fazer consulta de produto por ID")
        print("4. Fazer atualização de produto")
        print("5. Apagar produto")
        print("6. Sair")

        opcao2 = input("Digite qual opção: ")
        if opcao2 == "1":
            
            prod = Produto()

            prod.nome = input("Digite o nome: ")
            prod.marca = input("Digite a marca: ")
            prod.modelo = input("Digite o modelo: ")
            prod.descricao = input("Digite a descrição: ")
            prod.preco = float(input("Digite o preço: "))
            prod.tipo = input("Digite o tipo: ")
            prod.tamanho = int(input("Digite o tamanho: "))
            prod.peso = float(input("Digite o peso: "))

            result = prod.cadastrarProduto()
            if result == True:
                print("Cadastrado com Sucesso!!!")

        elif opcao2 == "2":
            prod = Produto()

            dados_do_banco = prod.selecionarProduto()

            for produto in dados_do_banco:
                print(f"id: {produto[0]} nome: {produto[1]} login: {produto[2]}")


        elif opcao2 == "3":
            prod = Produto()

            prod1 = int(input("Digite o id a consultar: "))

            produto = prod.selecionarProduto_por_id(prod1)

            print(produto)

            
        elif opcao2 == "4":

            id_prod = int(input("Digite o id: "))

            produto_selecionado = prod.selecionarProduto_por_id(id_prod)

            produto_selecionado[1] = input("DIGITE O NOVO NOME: ")
            produto_selecionado[2] = input("DIGITE A NOVA MARCA: ")
            produto_selecionado[3] = input("DIGITE O NOVO MODELO: ")
            produto_selecionado[4] = input("DIGITE A NOVA DESCRIÇÃO: ")
            produto_selecionado[5] = float(input("DIGITE O NOVO PREÇO: "))
            produto_selecionado[6] = input("DIGITE O NOVO TIPO: ")
            produto_selecionado[7] = int(input("DIGITE O NOVO TAMANHO: "))
            produto_selecionado[8] = float(input("DIGITE O NOVO PESO: "))

            atualizacao = prod.atualizarProduto(produto_selecionado)
            if atualizacao == True:
                print("Cliente atualizado com sucesso!!!")
                prod_atualizado = prod.selecionarProduto_por_id(produto_selecionado[0])
                print(prod_atualizado)

        elif opcao2 == "5":
            id_prod = int(input("Digite o ID: "))

            prod_deletado = prod.deletarProduto(id_prod)
            if prod_deletado == True:
                print("Deletado com sucesso!")
                dados_do_banco = prod.selecionarProduto()

                for produto in dados_do_banco:
                    print(f"id: {produto[0]} nome: {produto[1]} login: {produto[2]}")

        elif opcao2 == "6":
            print ("Saindo")
            continue

        else:
            print("Opção inválida.")


    elif opcao == "3":
        print("Saindo!")
        break
    
    else:
        print("Opção inválida.")


    





    

# cli1.nome = input("Digite o nome: ")
# cli1.cpf = input("Digite o cpf: ")
# cli1.email = input("Digite o email: ")
# cli1.fone = input("Digite o fome: ")
# cli1.endereco = input("Digite o endereco: ")
# cli1.cidade = input("Digite o cidade: ")

# result = cli1.cadastrar()
# if result == True:
#     print("Cadastrar com Sucesso!!!")

# cli1 = Cliente()

# dados_do_banco = cli1.selecionar()

# for cliente in dados_do_banco:
#     print(f"id: {cliente[0]} nome: {cliente[1]} login: {cliente[2]}")

# print("Atualizar dados!")
# id_cli = int(input("Digite o id: "))

# cliente_selecionado = cli1.selecionar_por_id(id_cli)

# cliente_selecionado[1] = input("DIGITE O NOVO NOME: ")
# cliente_selecionado[2] = input("DIGITE O NOVO CPF: ")
# cliente_selecionado[3] = input("DIGITE O NOVO EMAIL: ")
# cliente_selecionado[4] = input("DIGITE O NOVO FONE: ")
# cliente_selecionado[5] = input("DIGITE O NOVO ENDERECO: ")
# cliente_selecionado[6] = input("DIGITE O NOVO CIDADE: ")

# atualizacao = cli1.atualizar(cliente_selecionado)
# if atualizacao == True:
#     print("Cliente atualizado com sucesso!!!")
#     cli_atualizado = cli1.selecionar_por_id(cliente_selecionado[0])
#     print(cli_atualizado)

# else:
#     print("Erro ao atualizar!")

# print("Deseja deletar um cliente? ")
# id_cli = int(input("Digite o ID: "))

# cli_deletado = cli1.deletar(id_cli)
# if cli_deletado == True:
#     print("Deletado com sucesso!")
#     dados_do_banco = cli1.selecionar()

#     for cliente in dados_do_banco:
#         print(f"id: {cliente[0]} nome: {cliente[1]} login: {cliente[2]}")
