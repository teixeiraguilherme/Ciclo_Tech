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