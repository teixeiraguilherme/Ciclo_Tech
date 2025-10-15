import os
import time


aguardar = time.sleep



def limpar_tela():
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')



def validar_senha(teste):
    if len(teste)<8:
        return "A senha deve haver no mínimo 8 caracteres."
    letra=False
    numero=False
    for caractere in teste:
        if caractere.isalpha():
            letra=True
        elif caractere.isdigit():
            numero=True
        else:
            return "A senha não pode conter caracteres especiais."
    if not letra:
        return "A senha não contém letra"
    if not numero:
        return "A senha não contém número"
    return "Aprovada!"



def validar_email(email):
    posicao_arroba = email.find("@")
    posicao_ponto = email.rfind(".")
    if posicao_arroba > 0 and posicao_ponto > posicao_arroba + 1 and not email.endswith("."):
        if email.count("@") == 1:
            return True
    return
        
