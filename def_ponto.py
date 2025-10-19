from cadastro import carregar_usuarios, carregar_pontos, salvar_usuarios, salvar_pontos, email_existe
from utils import limpar_tela, aguardar, validar_senha, validar_email
import login
import menu_inicial
import json

def perfil_ponto(usuario_logado):
    limpar_tela()
    print("--- 🏢 MEU PERFIL ---")
    pontos = carregar_pontos()
    for ponto in pontos:
        endereco_format = usuario_logado.get('endereco')
        rua = endereco_format.get('rua')
        numero = endereco_format.get('numero')
        bairro = endereco_format.get('bairro')
        cidade = endereco_format.get('cidade')
        estado = endereco_format.get('estado')
        cep = endereco_format.get('cep')
    
    print(f"Nome: \t\t{usuario_logado.get('nome_ponto')}")
    print(f"Email: \t\t{usuario_logado.get('email')}")
    print(f"CNPJ: \t\t{usuario_logado.get('cnpj')}")
    print(f"Telefone: \t{usuario_logado.get('telefone')}")
    print(f"Endereço: \t{rua}, {numero}, {bairro}, {cidade} - {estado} / {cep}")
    aguardar(3) 

    print("\n[1] Editar perfil")
    print("[2] Editar endereço")
    print("[3] Excluir conta")
    print("[4] Redifinir senha")
    print("[0] Voltar menu anterior")

    try:
        entrada_perfil = int(input("\nEscolha uma opção: "))
        return entrada_perfil
    except:
        entrada_perfil = -1

def editar_ponto(usuario_logado):
    limpar_tela()
    print("--- ✏️ EDITAR PERFIL DO USUÁRIO ---")
    pontos = carregar_pontos()

    for ponto in pontos:
        if ponto['email'] == usuario_logado['email']:
            print("Deixe em branco para manter o valor atual.\n")
            while True:
                novo_nome = input(f"Nome ({ponto['nome_ponto']}): ")
                if novo_nome == "":
                    novo_nome = ponto['nome_ponto']
                    pass
                if len(novo_nome) > 4:
                    break
                else:
                    print("Nome muito curto, tente novamente.")
            while True:
                novo_telefone = input(f"Telefone ({ponto['telefone']}): ")
                novo_telefone_limpo = "".join(filter(str.isdigit, novo_telefone))
                if novo_telefone_limpo == "":
                    novo_telefone_limpo = ponto['telefone']
                    pass    
                if len(novo_telefone_limpo) == 11:
                    break
                else:
                    print("Telefone inválido, tente novamente.")
            while True:
                novo_email = input(f"Email ({ponto['email']}): ")
                if novo_email == "":
                    novo_email = ponto['email']
                    pass    
                if validar_email(novo_email):
                    if email_existe(novo_email):
                        print("❌ Ops! Esse email já está cadastrado. Tente outro.")
                    else:
                        break
                else:
                    print("Email inválido, tente novamente.")
            
            ponto['nome_ponto'] = novo_nome
            ponto['telefone'] = novo_telefone
            ponto['email'] = novo_email

            salvar_pontos(pontos)
            print("\n✅ Perfil atualizado com sucesso!")
            aguardar(2)
            return

def excluir_ponto(usuario_logado):
    limpar_tela()
    print("--- 🗑️ EXCLUIR CONTA DO PONTO ---")
    try:
        confirmacao = int(input("Tem certeza que deseja excluir sua conta? Esta ação é irreversível. \n [1] Sim [2] Não \n Escolha uma opção: "))
        return confirmacao
    except: 
        return -1
    
def editar_endereco(usuario_logado):
    limpar_tela()
    print("--- ✏️ EDITAR ENDEREÇO DO PONTO ---")
    pontos = carregar_pontos()

    for ponto in pontos:
        if ponto['email'] == usuario_logado['email']:
            endereco_atual = ponto.get('endereco', {})
            print("Deixe em branco para manter o valor atual.\n")
            nova_rua = input(f"Rua ({endereco_atual.get('rua', '')}): ") or endereco_atual.get('rua', '')
            novo_numero = input(f"Número ({endereco_atual.get('numero', '')}): ") or endereco_atual.get('numero', '')
            novo_bairro = input(f"Bairro ({endereco_atual.get('bairro', '')}): ") or endereco_atual.get('bairro', '')
            nova_cidade = input(f"Cidade ({endereco_atual.get('cidade', '')}): ") or endereco_atual.get('cidade', '')
            novo_estado = input(f"Estado ({endereco_atual.get('estado', '')}): ") or endereco_atual.get('estado', '')
            while True:
                novo_cep = input(f"Cep ({endereco_atual['cep']}): ")
                cep_limpo = "".join(filter(str.isdigit, novo_cep))
                if cep_limpo == '':
                    cep_limpo = endereco_atual['cep']
                    pass
                if len(cep_limpo) == 8:
                    break
                else:
                        print("Cep inválido, Tente novamente.")

            ponto['endereco'] = {
                'rua': nova_rua,
                'numero': novo_numero,
                'bairro': novo_bairro,
                'cidade': nova_cidade,
                'estado': novo_estado,
                'cep': novo_cep
            }

            salvar_pontos(pontos)
            print("\n✅ Endereço atualizado com sucesso!")
            aguardar(2)
            return