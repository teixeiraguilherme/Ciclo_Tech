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
        # A LINHA MAIS IMPORTANTE DO ARQUIVO:
        return entrada # <<--- DEVOLVE O NÚMERO PARA O MAIN.PY
    except ValueError:
        # Se der erro, devolve um número inválido
        return -1