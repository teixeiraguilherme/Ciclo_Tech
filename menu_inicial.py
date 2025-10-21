from utils import limpar_tela
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def menu_inicial():
    limpar_tela()
    console.print("______MENU INICIAL______\n", style="bold cyan")
    console.print("1 - TUTORIAL")
    console.print("2 - CADASTRO")
    console.print("3 - LOGIN")
    console.print("0 - FECHAR MENU")
    
    try:
        entrada = int(Prompt.ask("\nQual função deseja"))
        return entrada
    except:
        console.print("Entrada inválida! Digite um número válido.", style="bold red")
        return -1

def menu_ponto(usuario_logado):
    limpar_tela()
    console.print(f"--- 🏢 PAINEL DO PONTO ---", style="bold cyan")
    console.print(f"Bem-vindo(a), {usuario_logado['nome_ponto']}!\n", style="bold green")
    
    console.print("1. Cadastrar reciclagem")
    console.print("2. Impactos")
    console.print("3. Perfil")
    console.print("0. Sair")
    
    try: 
        entrada_usuario = int(Prompt.ask("\nEscolha uma opção"))
        return entrada_usuario
    except:
        console.print("Entrada inválida! Digite um número válido.", style="bold red")
        return -1

def menu_usuario(usuario_logado):
    limpar_tela()
    console.print(f"--- 👤 PAINEL DO USUÁRIO ---", style="bold cyan")
    console.print(f"Bem-vindo(a), {usuario_logado['nome']}!\n", style="bold green") 
    
    console.print("[1] Encontrar pontos de coleta")
    console.print("[2] Calcular pontuação")
    console.print("[3] Impactos")
    console.print("[4] Indicações")
    console.print("[5] Tutorial")
    console.print("[6] Meu perfil")
    console.print("[0] Sair da conta")
    
    try:
        entrada_usuario = int(Prompt.ask("\nEscolha uma opção"))
        return entrada_usuario
    except:
        console.print("Entrada inválida! Digite um número válido.", style="bold red")
        return -1
