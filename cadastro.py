from utils import limpar_tela, aguardar, validar_senha, validar_email
import requests
import json

def cadastro():
    escolher_cadastro = int(input(" 1- cadastro usuário \n 2- cadastro ponto\n 0- Voltar ao menu \nEscolha seu cadastro: "))
    if escolher_cadastro == 1:
        cadastro_usuario()
    elif escolher_cadastro == 2:
        cadastro_ponto()
    elif escolher_cadastro == 0:
        print("Voltando ao menu...")
        aguardar(2)
        return 
    else:
        print("Insira um número válido: ")

def endereco():
    while True:
        cep = str(input("Cep: "))
        cep_limpo = "".join(filter(str.isdigit, cep))
        if len(cep_limpo) == 8:
            break
        else:
            print("Cep inválido, Tente novamente.")
    rua = str(input("Rua: "))
    numero = str(input("Numero da casa: "))
    bairro = str(input("Bairro: "))
    cidade = str(input("Cidade: "))
    estado = str(input("Estado: "))
    pais = str(input("Pais: "))

    endereco_formatado = {
        "cep": cep_limpo,
        "rua": rua,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "pais": pais,
    }
    return endereco_formatado
    
def carregar_pontos():
    try:
        with open("pontos.json", "r", encoding = "utf-8") as arquivo_ponto:
            conteudo_ponto =  arquivo_ponto.read()
            if not conteudo_ponto:
                return []
            return json.loads(conteudo_ponto)
    except FileNotFoundError:
        with open("pontos.json", "w", encoding = "utf-8") as arquivo_ponto:
            json.dump([], arquivo_ponto)

def salvar_pontos(lista_de_pontos):
    with open("pontos.json", "w", encoding = "utf-8") as arquivo_ponto:
        json.dump(lista_de_pontos, arquivo_ponto, indent=4, ensure_ascii=False)

def email_existe(email_para_checar):
    usuarios = carregar_usuarios()
    pontos = carregar_pontos()

    for usuario in usuarios:
        if usuario['email'] == email_para_checar:
            return True 

    for ponto in pontos:
        if ponto['email'] == email_para_checar:
            return True 

    return False

def cpf_existe(cpf_checar):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario['cpf'] == cpf_checar:
            return True 

    return False

def cnpj_existe(cnpj_checar):
    pontos = carregar_pontos()

    for ponto in pontos:
        if ponto['cnpj'] == cnpj_checar:
            return True 

    return False



def cadastro_ponto():
    limpar_tela()
    while True:
        nome_ponto = str(input("Nome: "))
        if len(nome_ponto)<5:
            print("Digite um nome com no mínimo 5 caracteres.")
        else:
            break
        
        
    while True:
        cnpj = str(input("Cnpj: "))
        cnpj_limpo = "".join(filter(str.isdigit, cnpj))
        url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
        print(f"\nConsultando CNPJ {cnpj_limpo}, por favor aguarde...")
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                if cnpj_existe(cnpj_limpo):
                    print("❌ Ops! Esse CNPJ já está cadastrado. Tente outro.")
                    aguardar(2)
                    continue
                else: 
                    print("CNPJ Válido!")
                    aguardar(2)
                    break
                
            else:
                print(f"✖ ERRO: CNPJ não encontrado ou inválido. Tente novamente.")
                aguardar(2)
            
        except requests.exceptions.RequestException:
            print("✖ ERRO: Falha na conexão. Verifique sua internet e tente novamente.")
            aguardar(2)
    while True:
        telefone_ponto = str(input("Telefone(formato: *8199999-9999): "))
        numero_limpo_ponto = "".join(filter(str.isdigit, telefone_ponto))
        if len(numero_limpo_ponto) == 11:
            break  
        else:
            print("Número inválido, tente novamente...")

    while True:
        email_ponto = str(input("Email: "))
        if validar_email(email_ponto):
            if email_existe(email_ponto):
                print("❌ Ops! Esse email já está cadastrado. Tente outro.")
                aguardar(2)
            else:
                break
        else: 
            print("Email inválido, digite um correto")
        
    while True:
        confirmar_email_ponto = str(input("Confirme seu email: "))
        if email_ponto == confirmar_email_ponto:
            break
        else:
            print("Email's diferentes, tente novamento!")
    while True:
        print("****Senha deve conter no mínimo 8 carcateres, incluindo 1 número e 1 letra e sem carcatere especial****")
        senha_ponto = str(input("Criar uma senha: ")) 
        resultado = validar_senha(senha_ponto)
        if resultado == "Aprovada!":
            print("senha válida")
            break
        elif resultado == "A senha não contém letra":
            print("A senha não contém letra")
        elif resultado == "A senha não contém número":
            print("A senha não contém número")
        elif resultado == "A senha deve haver no mínimo 8 caracteres.":
            print("A senha deve haver no mínimo 8 caracteres.")
        elif resultado == "A senha não pode conter caracteres especiais.":
            print("A senha não pode conter caracteres especiais.")
        else:
            print("tente novamente")
    while True:
        confirmar_senha_ponto = str(input("Confirme sua senha: "))
        if senha_ponto != confirmar_senha_ponto:
            print("Senhas diferentes, tente novamento!")
            aguardar(2)
        elif senha_ponto == confirmar_senha_ponto:
            print("Senha criada")
            break
    endereco_formatado = endereco()
    while True:
        confirmar_cadastro_ponto = int(input("\n Confirmar cadastro \n [1] Sim \n[2] Não \n"))
        if confirmar_cadastro_ponto == 1:
            pontos_existentes = carregar_pontos()
            novo_ponto = {
                "nome_ponto": nome_ponto,
                "cnpj": cnpj_limpo,
                "telefone": numero_limpo_ponto,
                "email": email_ponto,
                "senha": senha_ponto,
                "endereco": endereco_formatado,
            }
            pontos_existentes.append(novo_ponto)
            salvar_pontos(pontos_existentes)
            print("CADASTRO EFETIVADO, PARABÉNS!!")
            aguardar(2)
            return
        elif confirmar_cadastro_ponto == 2:
            while True:
                reiniciar = int(input("Deseja reiniciar? \n [1] Sim \n[2] Não \n"))
                if reiniciar == 1:
                    print("Reiniciando cadastro...")
                    aguardar(2)
                    cadastro_ponto()
                elif reiniciar == 2:
                    break
        else: 
            print("Insira um número válido: ")

def carregar_usuarios():
    try:
        with open('usuarios.json', 'r', encoding= "utf-8") as arquivo_usuario:
            conteudo_usuario = arquivo_usuario.read()
            if not conteudo_usuario:
                return []
            return json.loads(conteudo_usuario)
    except FileNotFoundError:
        with open("usuarios.json", "w", encoding = "utf-8") as arquivo_usuario:
            json.dump([], arquivo_usuario)
        return []

def salvar_usuarios(lista_de_usuarios):
    with open('usuarios.json', 'w', encoding='utf-8') as arquivo_usuario:
        json.dump(lista_de_usuarios, arquivo_usuario, indent=4, ensure_ascii=False)

def cadastro_usuario():
    limpar_tela()
    while True:
        nome_usuario = str(input("Nome: "))
        if len(nome_usuario)<5:
            print("Digite um nome com no mínimo 5 caracteres.")
        else:
            break

    while True:
        cpf = str(input("Cpf: "))
        cpf_limpo = "".join(filter(str.isdigit, cpf))
        if len(cpf_limpo) == 11:
            if cpf_existe(cpf_limpo):
                print("❌ Ops! Esse CPF já está cadastrado. Tente outro.")
                aguardar(2)
            else:
                print("CPF com formato válido!")
                break
        else:
            print("O cpf é inválido. Ele deve conter 11 números.")

    cidade_usuario = str(input("Cidade: "))
    
    while True:
        telefone_usuario = str(input("Telefone(formato: *81999999999): "))
        numero_limpo_usuario = "".join(filter(str.isdigit, telefone_usuario))
        if len(numero_limpo_usuario) == 11:
            break  
        else:
            print("Número inválido, tente novamente...")

    while True:
        email_usuario = str(input("Email: "))
        if validar_email(email_usuario):
            if email_existe(email_usuario):
                print("❌ Ops! Esse email já está cadastrado. Tente outro.")
                aguardar(2)
            else:
                break
        else: 
            print("Email inválido, digite um correto")
    while True:
        confirmar_email_usuario = str(input("Confirme seu email: "))
        if email_usuario == confirmar_email_usuario:
            break
        else:
            print("Senhas diferentes, tente novamento!")
    
    while True:
        print("****Senha deve conter no mínimo 8 carcateres, incluindo 1 número e 1 letra e sem carcatere especial****")
        senha_usuario = str(input("Criar uma senha: ")) 
        resultado_senha_usuario = validar_senha(senha_usuario)
        if resultado_senha_usuario == "Aprovada!":
            print("senha válida")
            break
        elif resultado_senha_usuario == "A senha não contém letra":
            print("A senha não contém letra")
        elif resultado_senha_usuario == "A senha não contém número":
            print("A senha não contém número")
        elif resultado_senha_usuario == "A senha deve haver no mínimo 8 caracteres.":
            print("A senha deve haver no mínimo 8 caracteres.")
        elif resultado_senha_usuario == "A senha não pode conter caracteres especiais.":
            print("A senha não pode conter caracteres especiais.")
        else:
            print("tente novamente")

    while True:
        confirmar_senha_usuario = str(input("Confirme sua senha: "))
        if senha_usuario != confirmar_senha_usuario:
            print("Senhas diferentes, tente novamento!")
            aguardar(2)
        elif senha_usuario == confirmar_senha_usuario:
            print("Senha criada")
            break

    while True:
        confirmar_cadastro_usuario = int(input("\n Confirmar cadastro \n [1] Sim \n[2] Não \n"))
        if confirmar_cadastro_usuario == 1:
            usuarios_existentes = carregar_usuarios()
            novo_usuario = {
                "nome": nome_usuario,
                "cpf": cpf_limpo,
                "cidade": cidade_usuario,
                "telefone": numero_limpo_usuario,
                "email": email_usuario,
                "senha": senha_usuario 
            }
            
            usuarios_existentes.append(novo_usuario)
            salvar_usuarios(usuarios_existentes)

            print("CADASTRO EFETIVADO, PARABÉNS!!")
            aguardar(2)
            return 
        elif confirmar_cadastro_usuario == 2:
            while True:
                reiniciar_usuario = int(input("Deseja reiniciar? \n [1] Sim \n[2] Não \n"))
                if reiniciar_usuario == 1:
                    print("Reiniciando cadastro...")
                    aguardar(2)
                    cadastro_usuario()
                elif reiniciar_usuario == 2:
                    break
        else: 
            print("Insira um número válido: ")
    
def cadastro_reciclagem():
    pass  # Função placeholder para cadastro de reciclagem
