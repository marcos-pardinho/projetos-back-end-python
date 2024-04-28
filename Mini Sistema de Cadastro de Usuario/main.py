# criação de uma lista vazia para armazenar os usuários
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    print("Digite o nome do usuário: ")
    nome = input() # Solicita o nome do usuário
    usuarios.append(nome) # Adiciona o nome da lista de usuário
    print("Usuário cadastrado com sucesso!")
    
    # Função para exibir a lista de usuários cadastrados
def exibir_usuarios():
    if usuarios:  # Verificxa se há usuários na lista
        print("Usuários cadastrados:")
        for usuario in usuarios:  # Itera sobre cada usuários na lista
            print(usuario) # Imprime o nome do usuário
    else:
            print("Nenhum usuário cadastrado no sistema")    

# loop principal do sistema
while True:
    # Exibe as opções para o usuário
    print("\nEscolha uma opção: ")
    print("1. Cadastrar usuário")
    print("2. Exibir usuários cadastrados")
    print("3. Sair")
    
    opcao = input() # Solicita a opção escolhida pelo usuário
    
    if opcao == "1":
        cadastrar_usuario() # Chama a função para cadastrar um novo usuário
    elif opcao == "2":
        exibir_usuarios() # Chama a função para exibir os usuários cadastrado
    elif opcao == "3":
        print("Saindo do programa...") # Mensagem de saída
        break # Sai do loop principal e encerra o programa
    else:
        print("Opção inválida. Por favor escolha uma opção válida.")    