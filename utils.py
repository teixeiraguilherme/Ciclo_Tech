import os
import time
import requests
import random
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track

console = Console()
aguardar = time.sleep

''' FUNÇÕES DE APOIO VISUAL '''

def limpar_tela():
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")


def barra_progresso(texto="Processando", tempo=1.5):
    for _ in track(range(10), description=f"[green]{texto}..."):
        time.sleep(tempo / 10)


def confirmar_acao(mensagem):
    console.print(f"\n{mensagem}", style="bold yellow")
    console.print("[1] Sim", style="green")
    console.print("[2] Não", style="red")
    
    while True:
        try:
            entrada = input("\nEscolha uma opção: ")
            opcao = int(entrada)
            
            if opcao == 1:
                return True
            elif opcao == 2:
                return False
            else:
                console.print("❌ Opção inválida. Digite 1 ou 2.", style="red")
        except ValueError:
            console.print("❌ Formato inválido! Digite apenas números.", style="red")


def gerar_codigo_verificacao():
    return random.randint(1000, 9999)


def limpar_apenas_numeros(texto):
    return "".join(filter(str.isdigit, str(texto)))

'''VALIDADORES LÓGICOS (Retornam True/False ou msg de erro)''' 

def validar_senha(teste):
    if len(teste) < 8:
        return "A senha deve ter no mínimo 8 caracteres."
    letra = False
    numero = False
    for caractere in teste:
        if caractere.isalpha():
            letra = True
        elif caractere.isdigit():
            numero = True
        else:
            return "A senha não pode conter caracteres especiais."
    if not letra:
        return "A senha não contém letra"
    if not numero:
        return "A senha não contém número"
    return "Aprovada!"


def validar_email(email):
    if not email: return False
    posicao_arroba = email.find("@")
    posicao_ponto = email.rfind(".")
    if posicao_arroba > 0 and posicao_ponto > posicao_arroba + 1 and not email.endswith("."):
        if email.count("@") == 1:
            return True
    return False


def validar_telefone(telefone):
    limpo = limpar_apenas_numeros(telefone)
    if len(limpo) == 11:
        return True, limpo
    return False, limpo


def validar_cpf(cpf):
    limpo = limpar_apenas_numeros(cpf)
    if len(limpo) == 11:
        return True, limpo
    return False, limpo


def consultar_cnpj(cnpj):
    cnpj_limpo = limpar_apenas_numeros(cnpj)
    if len(cnpj_limpo) != 14:
        return False, "CNPJ deve ter 14 dígitos."
        
    try:
        response = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}")
        if response.status_code == 200:
            dados = response.json()
            info = {
                "nome": dados.get("razao_social", ""),
                "telefone": dados.get("ddd_telefone_1", ""),
                "email": dados.get("email", ""),
                "logradouro": dados.get("logradouro", ""),
                "numero": dados.get("numero", ""),
                "bairro": dados.get("bairro", ""),
                "municipio": dados.get("municipio", ""),
                "uf": dados.get("uf", "")
            }
            return True, info
        else:
            return False, "CNPJ não encontrado."
    except Exception as e:
        return False, f"Erro na conexão: {e}"

'''LOOPS DE INPUT'''

def solicitar_nome(atual=""):
    while True:
        msg = f"Nome ({atual})" if atual else "Nome completo"
        nome = Prompt.ask(msg)
        
        if atual and not nome: return atual
        if len(nome) >= 4: return nome
        
        console.print("❌ O nome deve ter no mínimo 4 caracteres.", style="red")


def solicitar_telefone(atual=""):
    while True:
        msg = f"Telefone DDD+9dig ({atual})" if atual else "Telefone (apenas números)"
        tel = Prompt.ask(msg)
        
        if atual and not tel: return atual
        
        valido, limpo = validar_telefone(tel)
        if valido:
            return limpo
        
        console.print("❌ Telefone inválido! Digite os 11 números (DDD + 9 dígitos).", style="red")


def solicitar_cpf(sistema, atual=""):
    while True:
        msg = f"CPF ({atual})" if atual else "CPF (apenas números)"
        cpf = Prompt.ask(msg)
        
        if atual and not cpf: return atual
        if atual and cpf == atual: return cpf 
        
        valido, limpo = validar_cpf(cpf)
        if not valido:
            console.print("❌ CPF inválido! Deve conter exatamente 11 números.", style="red")
            continue
            
        if sistema.cpf_existe(limpo):
            console.print("❌ Este CPF já está cadastrado em outra conta!", style="bold red")
            continue
            
        return limpo


def solicitar_senha_segura():
    while True:
        senha = Prompt.ask("Senha")
        
        resultado = validar_senha(senha)
        if resultado != "Aprovada!":
            console.print(f"❌ {resultado}", style="red")
            continue
            
        confirma = Prompt.ask("Confirme a senha")
        if senha == confirma:
            return senha
        console.print("❌ As senhas não conferem. Tente novamente.", style="red")


def solicitar_email_cadastro(sistema, atual=""):
    while True:
        msg = f"Email ({atual})" if atual else "Email"
        email = Prompt.ask(msg)
        
        if atual and not email: return atual
        if atual and email == atual: return email

        if not validar_email(email):
            console.print("❌ Formato de email inválido.", style="red")
            continue
            
        if sistema.email_existe(email):
            console.print("❌ Email já cadastrado! Tente outro.", style="bold red")
            continue
            
        confirma = Prompt.ask("Confirme o Email")
        if email != confirma:
            console.print("❌ Os emails digitados são diferentes! Tente novamente.", style="bold red")
            continue 
            
        return email


def consultar_cnpj_api(sistema=None):

    while True:
        cnpj_input = Prompt.ask("CNPJ (somente números)")
        barra_progresso("Consultando")
        
        valido, retorno = consultar_cnpj(cnpj_input)
        
        if valido:
            cnpj_limpo = limpar_apenas_numeros(cnpj_input)
            
            if sistema and sistema.cnpj_existe(cnpj_limpo):
                console.print("❌ Este CNPJ já está cadastrado no sistema!", style="bold red")
                if not confirmar_acao("Tentar outro CNPJ?"): return False, None
                continue

            retorno['cnpj_limpo'] = cnpj_limpo
            return True, retorno
        else:
            console.print(f"❌ {retorno}", style="red")
            if not confirmar_acao("Deseja tentar digitar o CNPJ novamente?"):
                return False, None