from cadastro import carregar_usuarios, carregar_pontos, salvar_usuarios, salvar_pontos
from utils import limpar_tela, aguardar, validar_senha, validar_email
from rich.console import Console
from rich.prompt import Prompt
console = Console()


def login():
    limpar_tela()
    console.print("--- 🔒 TELA DE LOGIN ---", style="bold green\n")
    print("[1] Logar")
    print("[2] Esqueci minha senha")
    print("[3] Voltar ao menu principal")
    opcao_login = input("\nEscolha uma opção: ")

    if opcao_login == '1':
        pass
    elif opcao_login == '2':
        esqueci_minha_senha()
        return login()  
    elif opcao_login == '0':
        return None, None  # <<< agora retorna tupla
    else:
        print("\nOpção inválida!")
        aguardar(1)
        return None, None

    while True:
        email_login = input("\nDigite seu email: ")

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
            console.print("--- 🔒 TELA DE LOGIN ---", style="bold green")
            continue

        print(f"\nEmail encontrado! Agora digite a senha.")
      
        while True:
            senha_login = input("\nDigite sua senha: ")

            if conta_encontrada['senha'] == senha_login:
                if tipo_conta == "usuario":
                    aguardar(2)
                    return "usuario", conta_encontrada  # <<< retorna conta correta
                elif tipo_conta == "ponto":
                    aguardar(2)
                    return "ponto", conta_encontrada
            
            else:
                print("\n❌ Senha incorreta")
                confirmar = input("Deseja redefinir a senha? [1] Sim [2] Não ")
                if confirmar == '1':
                    esqueci_minha_senha()
                    return login()  
                else:
                    print("Digite a senha novamente.")
                aguardar(1)

    return None, None  # <<< caso algum loop termine inesperadamente

def esqueci_minha_senha():
    limpar_tela()
    console.print("--- 🔑 RECUPERAÇÃO DE SENHA ---", style="bold cyan")
    email_rec = input("Digite o email da conta que você quer recuperar: ")

    if not validar_email(email_rec):
        print("\n❌ Formato de email inválido. Tente novamente.")
        aguardar(2)
        return None, None

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
                return None, None

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
                return None, None

    print("\n❌ Email não encontrado em nosso sistema.")
    aguardar(3)
    return None, None

def pedir_nova_senha_validada():
    while True:
        nova_senha = input("\nDigite sua nova senha: ")
        resultado_nova_senha = validar_senha(nova_senha)
        if resultado_nova_senha == "Aprovada!":
            confirmar_senha = input("\nConfirme sua nova senha: ")
            if nova_senha == confirmar_senha:
                return nova_senha 
            else:
                print("\n❌ As senhas não coincidem. Tente novamente.")
                
        elif resultado_nova_senha == "A senha não contém letra":
            print("A senha não contém letra")
        elif resultado_nova_senha == "A senha não contém número":
            print("A senha não contém número")
        elif resultado_nova_senha == "A senha deve haver no mínimo 8 caracteres.":
            print("A senha deve haver no mínimo 8 caracteres.")
        elif resultado_nova_senha == "A senha não pode conter caracteres especiais.":
            print("A senha não pode conter caracteres especiais.")
        else:
            print("Tente novamente")
