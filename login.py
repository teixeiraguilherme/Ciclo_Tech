# (Imports que você já tem no seu arquivo)
from cadastro import carregar_usuarios, carregar_pontos, salvar_usuarios, salvar_pontos
from utils import limpar_tela, aguardar, validar_senha, validar_email
import json

def login():
    limpar_tela()
    print("--- 🔒 TELA DE LOGIN ---")

    print("1. Logar")
    print("2. Esqueci minha senha")
    print("0. Voltar ao menu principal")
    opcao_login = input("\nEscolha uma opção: ")
    if opcao_login == '1':
        pass
    elif opcao_login == '2':
        esqueci_minha_senha()
        return login()  
    elif opcao_login == '0':
        return 
    else:
        print("\nOpção inválida!")
        aguardar(1)

    while True:
        email_login = input("Digite seu email: ")

        conta_encontrada = None
        tipo_conta = None 

        usuarios = carregar_usuarios()
        for usuario in usuarios:
            if usuario['email'] == email_login:
                conta_encontrada = usuario 
                tipo_conta = "usuario"
                break 

        if not conta_encontrada:
            pontos = carregar_pontos()
            for ponto in pontos:
                if ponto['email'] == email_login:
                    conta_encontrada = ponto 
                    tipo_conta = "ponto"
                    break
        
        
        if not conta_encontrada:
            print("\n❌ Email não cadastrado no sistema. Tente novamente.")
            aguardar(2)
            limpar_tela()
            print("--- 🔒 TELA DE LOGIN ---")
            continue

        print(f"\nEmail encontrado! Agora digite a senha.")
      
        while True:
            senha_login = input("Digite sua senha: ")

            if conta_encontrada['senha'] == senha_login:
                if tipo_conta == "usuario":
                    aguardar(2)
                    return "usuario", usuario

                
                elif tipo_conta == "ponto":
                    aguardar(2)
                    return "ponto", ponto
            
            else:
                print("\n❌ Senha incorreta")
                confirmar = input("Deseja redefinir a senha? [1] Sim [2] Não ")
                if confirmar == '1':
                    esqueci_minha_senha()
                    return login()  
                else:
                    print("digite a senha novamente.")
                aguardar(1)

def esqueci_minha_senha():
    limpar_tela()
    print("--- 🔑 RECUPERAÇÃO DE SENHA ---")
    email_rec = input("Digite o email da conta que você quer recuperar: ")

    if not validar_email(email_rec):
        print("\n❌ Formato de email inválido. Tente novamente.")
        aguardar(2)
        return

    usuarios = carregar_usuarios()
    for i, usuario in enumerate(usuarios):
        if usuario['email'] == email_rec:
            print(f"\nEncontramos a conta de usuário: {usuario.get('nome', 'Usuário')}")
            nova_senha = pedir_nova_senha_validada() 
            if nova_senha:
                usuarios[i]['senha'] = nova_senha
                salvar_usuarios(usuarios) 
                print("\n✅ Senha de USUÁRIO alterada com sucesso!")
                aguardar(2)
                return 

    pontos = carregar_pontos()
    for i, ponto in enumerate(pontos):
        if ponto['email'] == email_rec:
            print(f"\nEncontramos a conta de ponto de coleta: {ponto.get('nome_ponto', 'Ponto')}")
            nova_senha = pedir_nova_senha_validada()
            if nova_senha:
                pontos[i]['senha'] = nova_senha
                salvar_pontos(pontos) 
                print("\n✅ Senha de PONTO DE COLETA alterada com sucesso!")
                aguardar(2)
                return

    print("\n❌ Email não encontrado em nosso sistema.")
    aguardar(3)

def pedir_nova_senha_validada():
    while True:
        nova_senha = input("Digite sua nova senha: ")
        resultado_nova_senha = validar_senha(nova_senha)
        if resultado_nova_senha == "Aprovada!":
            confirmar_senha = input("Confirme sua nova senha: ")
            if nova_senha == confirmar_senha:
                return nova_senha 
            else:
                print("\n    ❌ As senhas não coincidem. Tente novamente.")
                
        elif resultado_nova_senha == "A senha não contém letra":
            print("A senha não contém letra")
        elif resultado_nova_senha == "A senha não contém número":
            print("A senha não contém número")
        elif resultado_nova_senha == "A senha deve haver no mínimo 8 caracteres.":
            print("A senha deve haver no mínimo 8 caracteres.")
        elif resultado_nova_senha == "A senha não pode conter caracteres especiais.":
            print("A senha não pode conter caracteres especiais.")
        else:
            print("tente novamente")
