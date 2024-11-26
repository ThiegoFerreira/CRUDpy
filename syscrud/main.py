from Entity.Pessoa import Pessoa

escolha = int(input("Escolha (1) para cadastar, escolha (2) para listar, escolha (3) atualizar, escolha(4) para deletar e escolha (0) para sair: "))

while escolha != 0:
    try:
        if escolha == 1:
            escolha2 = int(input("Escolha (1) para cadastrar usuário, escolha (2) para cadastrar produto, escolha (0) para sair: "))
            while escolha2 != 0:
                # try:
                    if escolha2 == 1:
                        nome = input("Digite o nome: ")
                        email = input("Digite o email: ")
                        fone = input("Digite o telefone: ")
                        endereco = input("Digite o endereço: ")
                        cidade = input("Digite a cidade: ")
                        tupla = (nome,email,fone,endereco,cidade)
                        bd = 

                        
                    elif escolha2 == 2:
                        nome = input("Digite o nome: ")
                        marca = input("Digite a marca: ")
                        modelo = input("Digite o modelo: ")
                        descricao = input("Digite a descricao: ")
                        preco = input("Digite o preco: ")
                        tipo = input("Digite o tipo: ")
                        tamanho = input("Digite o tamanho: ")
                        peso = input("Digite o peso: ")
                        tupla = (nome,marca,modelo,descricao,preco,tipo,tamanho,peso)
                        print(tupla)
                        escolha2 = int(input("Escolha (1) para cadastrar usuário, escolha (2) para cadastrar produto, escolha (0) para sair: "))

                    elif escolha2 ==0:
                        break
                        

                # except:

                #     escolha2 = int(input("Escolha (1) para cadastrar usuário, escolha (2) para cadastrar produto, escolha (0) para sair: "))

            
        elif escolha ==2:
            escolha2 = int(input("Escolha (1) para listar usuário, escolha (2) para listar produto, escolha (0) para sair: "))
        elif escolha ==3:
            escolha2 = int(input("Escolha (1) para atualizar usuário, escolha (2) para atualizar produto, escolha (0) para sair: "))
        elif escolha ==4:
            escolha2 = int(input("Escolha (1) para deletar usuário, escolha (2) para deletar produto, escolha (0) para sair: "))    

    except:
        escolha = int(input("Escolha (1) para cadastar, escolha (2) para listar, escolha (3) atualizar, escolha(4) para deletar e escolha (0) para sair: "))
