import menu_inicial
from utils import limpar_tela, aguardar, validar_senha
import tutorial
#import login
import cadastro

while True:
    entrada = menu_inicial.menu_inicial()
    if entrada == 1: 
        limpar_tela()
        print("Chamando a função de tutorial...")
        aguardar(1)
        tutorial.tutorial()
    elif entrada == 2:
        limpar_tela()
        aguardar(1)
        print("Chamando a função de cadastro...")
        cadastro.cadastro()
    elif entrada == 3:
        limpar_tela()
        aguardar(1)
        print("Chamando a função de login...")
        # login.login() 

    elif entrada == 0:
        print("Menu fechado.")
        break 
    
    else:
        print("\nDigite um número válido!\n")
        aguardar(2)





