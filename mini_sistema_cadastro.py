print('*' * 30)
print('Bem-vindo ao Mini Sistema de Cadastro')
print('*' * 30)
print('*' * 30)
print('1. Adicionar usuário')
print('2. Listar usuários')
print('3. Sair')
print('*' * 30)
print('*' * 30)

cadastro = {}
def adicionar_usuario(Nome, idade):   
    if Nome in cadastro:
        print(f"Usuário '{Nome}' já existe! Não é possível adicionar um novo usuário com esse nome.")
    else:
        cadastro[Nome] = idade
        print(f"Usuário '{Nome}' adicionado com idade '{idade}' com sucesso!")
def listar_usuarios():
    if not cadastro:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for Nome, idade in cadastro.items():
            print(f"Nome: {Nome}, Idade: {idade}")
while True:
    escolha = input("Escolha uma opção (1, 2 ou 3): ")
    
    if escolha == '1':
        nome_usuario = input("Digite o nome do usuário: ")
        if not nome_usuario.strip():
            print("Nome inválido! Por favor, insira um nome para o usuário.")
            continue
        idade_usuario = input("Digite a idade do usuário: ")
        if not idade_usuario.isdigit():
            print("Idade inválida! Por favor, insira um número para a idade.")
            continue
        adicionar_usuario(nome_usuario, idade_usuario)
    elif escolha == '2':
        listar_usuarios()
    elif escolha == '3':
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida! Por favor, escolha 1, 2 ou 3.")