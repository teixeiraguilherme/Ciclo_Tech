from cadastro import carregar_usuarios, carregar_pontos, salvar_usuarios, salvar_pontos, email_existe
from utils import limpar_tela, aguardar, validar_senha, validar_email
import login
import menu_inicial
import json
from rich.console import Console
from rich.prompt import Prompt

console = Console()


def procurar_pontos():
    pontos = carregar_pontos()
    

    print ("\n--- PONTOS DE COLETA CADASTRADOS ---\n")
    for ponto in pontos:
        endereco_format = ponto.get('endereco')
        rua = endereco_format.get('rua')
        numero = endereco_format.get('numero')
        bairro = endereco_format.get('bairro')
        cidade = endereco_format.get('cidade')
        estado = endereco_format.get('estado')
        cep = endereco_format.get('cep')
        print(f"\nNome: \t\t{ponto.get('nome_ponto')}")
        print(f"Endereço: \t{rua}, {numero}, {bairro}, {cidade} - {estado} / {cep}")   
        print(f"Email: \t\t{ponto.get('email')}")
        print(f"Telefone: \t{ponto.get('telefone')}")
        print(f"CNPJ: \t\t{ponto.get('cnpj')}\n")
        print("-------------------------------")


def perfil_usuario(usuario_logado):
    limpar_tela()
    console.print("--- 👤 MEU PERFIL ---", style = "bold green")
    print(f"Nome: \t\t{usuario_logado.get('nome')}")
    print(f"Email: \t\t{usuario_logado.get('email')}")
    print(f"CPF: \t\t{usuario_logado.get('cpf')}")
    print(f"Telefone: \t{usuario_logado.get('telefone')}")
    print(f"Cidade: \t{usuario_logado.get('cidade')}")
    aguardar(3) 

    console.print("\n[1] Editar perfil")
    console.print("[2] Excluir conta")
    console.print("[3] Redifinir senha")
    console.print("[0] Voltar menu anterior")

    try:
        entrada_perfil = int(input("\nEscolha uma opção: "))
        return entrada_perfil
    except:
        entrada_perfil = -1

def editar_usuario(usuario_logado):
    limpar_tela()
    console.print("--- ✏️ EDITAR PERFIL DO USUÁRIO ---", style="bold green")
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario['email'] == usuario_logado['email']:
            print("Deixe em branco para manter o valor atual.\n")
            while True:
                novo_nome = input(f"Nome ({usuario['nome']}): ")
                if novo_nome == "":
                    novo_nome = usuario['nome']
                    pass
                if len(novo_nome) > 4:
                    break
                else:
                    print("Nome muito curto, tente novamente.")

            while True:
                novo_telefone = input(f"\nTelefone ({usuario['telefone']}): ")
                novo_telefone_limpo = "".join(filter(str.isdigit, novo_telefone))
                if novo_telefone_limpo == "":
                    novo_telefone_limpo = usuario['telefone']
                    pass    
                if len(novo_telefone_limpo) == 11:
                    break
                else:
                    print("Telefone inválido, tente novamente.")
            nova_cidade = input(f"\nCidade ({usuario['cidade']}): ") or usuario['cidade']

            while True:
                novo_email = input(f"\nEmail ({usuario['email']}): ")
                if novo_email == "":
                    novo_email = usuario['email']
                    break    
                elif validar_email(novo_email):
                    if email_existe(novo_email):
                        print("❌ Ops! Esse email já está cadastrado. Tente outro.")
                    else:
                        break
                else:
                    print("Email inválido, tente novamente.")

            
            usuario['nome'] = novo_nome
            usuario['telefone'] = novo_telefone_limpo
            usuario['cidade'] = nova_cidade
            usuario['email'] = novo_email

            salvar_usuarios(usuarios)
            print("\n✅ Perfil atualizado com sucesso!")
            aguardar(2)
            return

def excluir_usuario(usuario_logado):
    limpar_tela()
    print("--- 🗑️ EXCLUIR CONTA DO USUÁRIO ---")
    try:
        confirmacao = int(input("Tem certeza que deseja excluir sua conta? Esta ação é irreversível. \n [1] Sim [2] Não \n Escolha uma opção: "))
        return confirmacao
    except: 
        return -1