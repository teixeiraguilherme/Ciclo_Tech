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

'''MENUS DE NAVEGAÇÃO'''

def menu_usuario_logado(user):
    while True:
        cabecalho()
        console.print(f"Bem-vindo, {user.nome} | 💎 {user.pontos}", style="green", justify="center")
        
        t = Table(show_header=False, box=None)
        t.add_row("[1] Ranking", "[2] Calculadora")
        t.add_row("[3] Impactos", "[4] Perfil")
        t.add_row("[5] Encontrar Pontos", "[0] Sair","")
        console.print(Align.center(t))
        
        op = pedir_opcao()
        if op == 0: break
        elif op == 1:
            cabecalho()
            for i, u in enumerate(app.gerar_ranking()):
                print(f"{i+1}. {u.nome} - {u.pontos} pts")
            input("\nVoltar...")
        elif op == 2:
            cabecalho()
            app.interface_calculadora()
        elif op == 3:
            cabecalho()
            app.interface_impactos(user)
        elif op == 4:
            while True:
                cabecalho()
                t = Table(title=f"Perfil: {user.nome}", box=box.ROUNDED, show_header=False)
                t.add_column("C", style="cyan"); t.add_column("V", style="white")
                t.add_row("Email", user.email); t.add_row("Tel", user.telefone)
                t.add_row("Cidade", user.cidade); t.add_row("CPF", user.cpf)
                console.print(Align.center(t))
                
                console.print("\n[1] Editar  [2] Trocar Senha  [3] Voltar", justify="center")
                sub_op = pedir_opcao()
                
                if sub_op == 1:
                    user.editar_perfil_interativo(app)
                    
                elif sub_op == 2:
                    app.interface_trocar_senha_logado(user)
                elif sub_op == 3: break

        elif op == 5:
            cabecalho()
            app.interface_encontrar_pontos()


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
            while True:
                cabecalho()
                t = Table(title=f"Perfil: {ponto.nome}", box=box.ROUNDED, show_header=False)
                t.add_column("C", style="magenta"); t.add_column("V", style="white")
                t.add_row("Email", ponto.email); t.add_row("CNPJ", ponto.cnpj)
                t.add_row("Tel", ponto.telefone)
                console.print(Align.center(t))
                
                console.print("\n[1] Editar  [2] Trocar Senha  [3] Voltar")
                sub_op = pedir_opcao()
                
                if sub_op == 1:
                    ponto.editar_perfil_interativo(app)
                    
                elif sub_op == 2:
                    app.interface_trocar_senha_logado(ponto)
                elif sub_op == 3: break

'''LOOP PRINCIPAL'''

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