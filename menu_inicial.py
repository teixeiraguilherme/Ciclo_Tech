from utils import limpar_tela

def menu_inicial():
    limpar_tela()
    print("______MENU INICIAL______\n")
    print("1 - TUTORIAL")
    print("2 - CADASTRO")
    print("3 - LOGIN")
    print("0 - FECHAR MENU")
    
    try:
        entrada = int(input("\nQual função deseja: "))
        return entrada
    except ValueError:
        return -1



def menu_ponto(usuario_logado):
    limpar_tela()
    print(f"--- 🏢 PAINEL DO PONTO ---")
    print(f"Bem-vindo(a), {usuario_logado['nome_ponto']}!")
    
    print("\n1. Cadastrar reciclagem")
    print("2. Impactos")
    print("3. Perfil")
    print("0. Sair")
    
    try: 
        entrada_usuario = int(input("\nEscolha uma opção: "))
        return entrada_usuario
    except:
        return -1
    


def menu_usuario(usuario_logado):
    limpar_tela()
    print(f"--- 👤 PAINEL DO USUÁRIO ---")
    print(f"Bem-vindo(a), {usuario_logado['nome']}!") 
    
    print("\n[1] Encontrar pontos de coleta")
    print("[2] Calcular pontuação")
    print("[3] Impactos")
    print("[4] Indicações")
    print("[5] Tutorial")
    print("[6] Meu perfil")
    print("[0] Sair da conta")
    
    try:
        entrada_usuario = int(input("\nEscolha uma opção: "))
        return entrada_usuario
    except:
        return -1
