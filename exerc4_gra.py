# Base de Dados de Usuários
database = []

# Função para criar um novo usuário
# Lista de campos que são obrigatórios para cada usuário
def criar_usuario(campos_obrigatorios):
    usuario = {}
    for campo in campos_obrigatorios:
        valor = input(f"Favor, insira o '{campo}' obrigatório: ")
        usuario[campo] = valor
    while True:
        campo_adicional = input("Digite um campo adicional (ou 'terminar' para concluir): ")
        if campo_adicional.lower() == 'terminar':
            break
        valor = input(f"Digite o valor para '{campo_adicional}': ")
        usuario[campo_adicional] = valor
    database.append(usuario)
    print("Usuário cadastrado!")

# Função para exibir informações dos usuários
# Aqui serâo utilizados if e elif para comparação da opções digitadas
def exibir_usuarios(*args, **kwargs):
    opcao = input("Escolha uma opção:\n1 - Exibir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\n")
    
    if opcao == '1':
        for usuario in database:
            print(usuario)
    elif opcao == '2':
        nomes = args
        for usuario in database:
            if usuario['nome'] in nomes:
                print(usuario)
    elif opcao == '3':
        campos = kwargs.keys()
        for usuario in database:
            if all(usuario.get(campo) == kwargs[campo] for campo in campos):
                print(usuario)
    elif opcao == '4':
        nomes = args
        campos = kwargs.keys()
        for usuario in database:
            if usuario['nome'] in nomes and all(usuario.get(campo) == kwargs[campo] for campo in campos):
                print(usuario)
    else:
        print("Opção inválida")

# Função principal
def iniciar():
    campos_obrigatorios = input("Informe os campos obrigatórios separados por vírgula: ").split(',')
# Enquanto o while for verdadeiro, a estrutura se repete
    while True:
        print("\nMenu:")
        print("1 - Criar usuário")
        print("2 - Exibir usuários")
        print("0 - Fechar Programa")
        
        escolha = input("Escolher opção: ")
        
        if escolha == '1':
            criar_usuario(campos_obrigatorios)
        elif escolha == '2':
            exibir_usuarios()
        elif escolha == '0':
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    iniciar()
