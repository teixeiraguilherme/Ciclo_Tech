from sistema import SistemaCiclotech
from tutorial import tutorial
import utils
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich import box

console = Console()
app = SistemaCiclotech()

def cabecalho():
    utils.limpar_tela()
    console.print(Panel(Align.center("[bold green]♻️  CICLOTECH  ♻️[/]"), border_style="green"))


def pedir_opcao():
    while True:
        try: return int(input("\nOpção: "))
        except: console.print("❌ Digite um número.", style="red")

'''===================================='''
'''              MENUS                 '''
'''===================================='''

def menu_usuario_logado(user):
    while True:
        cabecalho()
        console.print(f"Bem-vindo, {user.nome} | 💎 {user.pontos}", style="green", justify="center")
        
        t = Table(show_header=False, box=None)
        t.add_row("[1] Ranking", "[2] Calculadora")
        t.add_row("[3] Impactos", "[4] Perfil")
        t.add_row("[5] Encontrar Pontos", "[6] Indicações")
        t.add_row("[0] Sair""")
        console.print(Align.center(t))
        
        op = pedir_opcao()
        if op == 0: break
        elif op == 1:
            cabecalho()
            app.interface_ranking(user)
        elif op == 2:
            cabecalho()
            app.interface_calculadora()
        elif op == 3:
            cabecalho()
            app.interface_impactos(user)
        elif op == 4:
            cabecalho()
            app.interface_perfil_user(user)
        elif op == 5:
            cabecalho()
            app.interface_encontrar_pontos()
        elif op == 6:
            cabecalho()
            app.interface_indicacao()
        else:
            console.print("❌ Opção inválida.", style="red")
            utils.aguardar(2)


def menu_ponto_logado(ponto):
    while True:
        cabecalho()
        console.print(f"Painel: {ponto.nome}", style="magenta", justify="center")
        t = Table(show_header=False, box=None)
        t.add_row("[1] Registrar Reciclagem", "[2] Perfil/Dados")
        t.add_row("[0] Sair", "")
        console.print(Align.center(t))
        
        op = pedir_opcao()
        if op == 0: break
        elif op == 1:
            cabecalho()
            app.interface_registrar_reciclagem()
        elif op == 2:
            cabecalho()
            app.interface_perfil_ponto(ponto)
        else:
            console.print("❌ Opção inválida.", style="red")
            utils.aguardar(2)

'''===================================='''
'''          LOOP PRINCIPAL            '''
'''===================================='''

while True:
    utils.limpar_tela()
    cabecalho()
    menu = Table(show_header=False, box=None, padding=(1, 4))
    
    menu.add_column(justify="right") 
    menu.add_column(justify="left")
    menu.add_row("[bold cyan][1][/] 📖 Tutorial", "[bold cyan][2][/] 📝 Cadastro"
                 ,"[bold cyan][3][/] 🔐 Login",  "[bold cyan][0][/] 🚪 Sair""")

    console.print(Align.center(menu))
    print("\n")
    
    op = pedir_opcao()
    
    if op == 1: 
        tutorial()
        
    elif op == 2:
        utils.limpar_tela()
        console.print("--- CADASTRO ---", style="bold green")
        console.print("[1] Usuário Comum (Reciclador)")
        console.print("[2] Ponto de Coleta (Empresa)")
        console.print("[Enter] para voltar...")
        try:
            op_cad = int(input("\nTipo de conta: "))
            if op_cad == 1: app.interface_cadastro_usuario()
            elif op_cad == 2: app.interface_cadastro_ponto()
        except ValueError: pass
        
    elif op == 3:
        tipo, obj = app.interface_login()
        
        if obj:
            if tipo == 'usuario': 
                menu_usuario_logado(obj)
            else: 
                menu_ponto_logado(obj)

    elif op == 0: 
        console.print("Saindo... Até logo! 👋", style="green")
        break