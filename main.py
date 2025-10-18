import menu_inicial
from utils import limpar_tela, aguardar
import tutorial
import login
import cadastro
from menu_usuario import menu_usuario
from menu_ponto import menu_ponto

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
        tipo_usuario, nome_usuario = login.login() 
        if tipo_usuario == "usuario":
            menu_usuario(nome_usuario) 
        elif tipo_usuario == "ponto":
            menu_ponto(nome_usuario)

    elif entrada == 0:
        print("Menu fechado.")
        break 
    
    else:
        print("\nDigite um número válido!\n")
        aguardar(2)