from utils import limpar_tela, aguardar, validar_senha

def cadastro():
    escolher_cadastro = int(input(" 1- cadastro usuário \n 2- cadastro ponto\n Escolha seu cadastro: "))
    if escolher_cadastro == 1:
        cadastro_usuario()
    elif escolher_cadastro == 2:
        cadastro_ponto()
    else:
        print("Insira um número válido: ")

def endereco():
    cep = int(input("Cep: "))
    rua = str(input("Rua: "))
    numero = int(input("Numero: "))
    bairro = str(input("Bairro: "))
    cidade = str(input("Cidade: "))
    estado = str(input("Estado: "))
    pais = str(input("Pais: "))

def cadastro_ponto():
    try:
        limpar_tela()
        nome_ponto = str(input("Nome: "))
        cnpj = int(input("Cnpj: "))
        telefone_ponto = int(input("Telefone: "))
        email_ponto = str(input("Email: "))
        confirmar_email_ponto = str(input("Confirme seu email: "))
        if email_ponto != confirmar_email_ponto:
            print("Senhas diferentes, tente novamento!")
            cadastro_ponto()
            #voltar apenas para a email
        while True:
            senha_ponto = str(input("Criar uma senha: "))
            resultado_validacao = validar_senha(senha_ponto) 
            if resultado_validacao == "OK":
                print("Senha forte e válida!")
                aguardar(1)
                break
            else:
                print(f"Senha inválida: {resultado_validacao}")
                aguardar(3)
                cadastro_usuario()
            confirmar_senha_ponto = str(input("Confirme sua senha: "))
            if senha_ponto != confirmar_senha_ponto:
                print("Senhas diferentes, tente novamento!")
                aguardar(2)
                cadastro_ponto()
                #voltar apenas para a senha
        endereco()
        confirmar_cadastro_ponto = str(input("\n1- Sim \n2- Não \n Confirma cadastro: "))
        if confirmar_cadastro_ponto == 1:
            print("CADASTRO EFETIVADO, PARABÉNS!!")
            aguardar(2)
        elif confirmar_cadastro_ponto == 2:
            print("Reiniciando cadastro...")
            #voltar apenas para a parte desejavel.
            aguardar(2)
            cadastro_ponto()
        else: 
            print("Insira um número válido: ")
    except:
            print("Você inseriu caracteres inválidos em algum campo")
            aguardar(2)
            cadastro_usuario()

def cadastro_usuario():
    #try:
        limpar_tela()
        nome_usuario = str(input("Nome: "))
        idade_usuario = int(input("Idade: "))
        cpf = int(input("Cpf: "))
        cidade_usuario = str(input("Cidade: "))
        telefone_usuario = int(input("Telefone: "))
        email_usuario = str(input("Email: "))
        confirmar_email_usuario = str(input("Confirme seu email: "))
        if email_usuario != confirmar_email_usuario:
            print("Email diferentes, tente novamento!")
            cadastro_usuario()
            #voltar apenas para a email
        senha_usuario = str(input("Criar uma senha: "))
        while True:
            senha_usuario = str(input("Criar uma senha: "))
            resultado_validacao_usuario = validar_senha(senha_usuario) 
            if resultado_validacao_usuario == "OK":
                print("Senha forte e válida!")
                aguardar(1)
                break
            else:
                print(f"Senha inválida: {resultado_validacao_usuario}")
                aguardar(3)
                cadastro_usuario()
        confirmar_senha_usuario = str(input("Confirme sua senha: "))
        if senha_usuario != confirmar_senha_usuario:
            print("Senhas diferentes, tente novamento!")
            aguardar(2)
            cadastro_usuario()
            #voltar apenas para a senha
        confirmar_cadastro_usuario = str(input("\n1- Sim \n2- Não \n Confirma cadastro: "))
        if confirmar_cadastro_usuario == 1:
            print("CADASTRO EFETIVADO, PARABÉNS!!")
            aguardar(2)
        elif confirmar_cadastro_usuario == 2:
            print("Reiniciando cadastro...")
            aguardar(2)
            cadastro_usuario()
        else: 
            print("Insira um número válido: ")
    989898898989989898
