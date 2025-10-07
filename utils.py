import os
import time

aguardar = time.sleep

def limpar_tela():
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')


def validar_senha():
    """
    Valida uma senha de acordo com os critérios de segurança.
    Retorna True se a senha for válida, e uma mensagem de erro se for inválida.
    """
    # Critérios
    min_comprimento = 8
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    # 1. Verifica o comprimento mínimo
    if len() < min_comprimento:
        return f"A senha deve ter pelo menos {min_comprimento} caracteres."

    # 2. Verifica cada caractere
    for char in ():
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        # Verifica se é um caractere especial (não é letra nem número)
        elif not char.isalnum():
            tem_especial = True
    
    # 3. Verifica se todos os critérios foram atendidos
    if not tem_maiuscula:
        return "A senha deve conter pelo menos uma letra maiúscula (A-Z)."
    if not tem_minuscula:
        return "A senha deve conter pelo menos uma letra minúscula (a-z)."
    if not tem_numero:
        return "A senha deve conter pelo menos um número (0-9)."
    if not tem_especial:
        return "A senha deve conter pelo menos um caractere especial (ex: !@#$%)."
        
    # Se passou por todas as verificações, a senha é forte
    return "OK"