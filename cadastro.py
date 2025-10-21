import json
import requests
from utils import limpar_tela, aguardar, validar_senha, validar_email
from rich.console import Console
from rich.prompt import Prompt

console = Console()

# ---------- CARREGAR / SALVAR USUÁRIOS ----------
def carregar_usuarios():
    try:
        with open('usuarios.json', 'r', encoding= "utf-8") as arquivo:
            conteudo = arquivo.read()
            if not conteudo:
                return []
            return json.loads(conteudo)
    except FileNotFoundError:
        with open("usuarios.json", "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo)
        return []

def salvar_usuarios(lista):
    with open('usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

# ---------- CARREGAR / SALVAR PONTOS ----------
def carregar_pontos():
    try:
        with open("pontos.json", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if not conteudo:
                return []
            return json.loads(conteudo)
    except FileNotFoundError:
        with open("pontos.json", "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo)
        return []

def salvar_pontos(lista):
    with open("pontos.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

# ---------- VALIDAÇÕES ----------
def email_existe(email):
    usuarios = carregar_usuarios()
    pontos = carregar_pontos()
    return any(u['email']==email for u in usuarios) or any(p['email']==email for p in pontos)

def cpf_existe(cpf):
    usuarios = carregar_usuarios()
    return any(u['cpf']==cpf for u in usuarios)

def cnpj_existe(cnpj):
    pontos = carregar_pontos()
    return any(p['cnpj']==cnpj for p in pontos)

# ---------- ENDEREÇO ----------
def endereco():
    while True:
        cep = Prompt.ask("Cep")
        cep_limpo = "".join(filter(str.isdigit, cep))
        if len(cep_limpo) == 8:
            break
        console.print("Cep inválido, tente novamente.", style="bold red")
    
    rua = Prompt.ask("Rua")
    numero = Prompt.ask("Número da casa")
    bairro = Prompt.ask("Bairro")
    cidade = Prompt.ask("Cidade")
    estado = Prompt.ask("Estado")
    pais = Prompt.ask("País")

    return {
        "cep": cep_limpo,
        "rua": rua,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "pais": pais,
    }

# ---------- CADASTRO DE USUÁRIO ----------
def cadastro_usuario():
    limpar_tela()
    while True:
        nome = Prompt.ask("Nome")
        if len(nome) < 5:
            console.print("Digite um nome com no mínimo 5 caracteres.", style="bold red")
        else:
            break

    while True:
        cpf = "".join(filter(str.isdigit, Prompt.ask("CPF")))
        if len(cpf) == 11:
            if cpf_existe(cpf):
                console.print("❌ CPF já cadastrado. Tente outro.", style="bold red")
                aguardar(2)
            else:
                break
        else:
            console.print("CPF inválido. Deve conter 11 números.", style="bold red")

    cidade = Prompt.ask("Cidade")

    while True:
        telefone = "".join(filter(str.isdigit, Prompt.ask("Telefone (11 dígitos)")))
        if len(telefone) == 11:
            break
        console.print("Número inválido, tente novamente.", style="bold red")

    while True:
        email = Prompt.ask("Email")
        if validar_email(email):
            if email_existe(email):
                console.print("❌ Email já cadastrado. Tente outro.", style="bold red")
                aguardar(2)
            else:
                break
        else:
            console.print("Email inválido.", style="bold red")

    while True:
        confirmar_email = Prompt.ask("Confirme seu email")
        if email == confirmar_email:
            break
        console.print("Emails diferentes, tente novamente.", style="bold red")

    while True:
        console.print("Senha deve conter 8+ caracteres, 1 letra e 1 número, sem caracteres especiais.", style="bold cyan")
        senha = Prompt.ask("Criar senha", password=True)
        resultado = validar_senha(senha)
        if resultado == "Aprovada!":
            break
        console.print(resultado, style="bold red")

    while True:
        confirmar_senha = Prompt.ask("Confirme sua senha", password=True)
        if senha == confirmar_senha:
            break
        console.print("Senhas diferentes, tente novamente.", style="bold red")

    while True:
        confirmar = int(Prompt.ask("\nConfirmar cadastro? [1] Sim [2] Não"))
        if confirmar == 1:
            usuarios = carregar_usuarios()
            usuarios.append({
                "nome": nome,
                "cpf": cpf,
                "cidade": cidade,
                "telefone": telefone,
                "email": email,
                "senha": senha
            })
            salvar_usuarios(usuarios)
            console.print("✅ Cadastro de usuário efetuado!", style="bold green")
            aguardar(2)
            return
        elif confirmar == 2:
            if int(Prompt.ask("Deseja reiniciar? [1] Sim [2] Não")) == 1:
                cadastro_usuario()
            return

# ---------- CADASTRO DE PONTO ----------
def cadastro_ponto():
    limpar_tela()
    while True:
        nome_ponto = Prompt.ask("Nome do ponto")
        if len(nome_ponto) < 5:
            console.print("Digite um nome com no mínimo 5 caracteres.", style="bold red")
        else:
            break

    while True:
        cnpj = "".join(filter(str.isdigit, Prompt.ask("CNPJ")))
        url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
        console.print(f"Consultando CNPJ {cnpj}...", style="bold cyan")

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                if cnpj_existe(cnpj):
                    console.print("❌ CNPJ já cadastrado. Tente outro.", style="bold red")
                    aguardar(2)
                    continue
                break
            else:
                console.print("✖ CNPJ inválido. Tente novamente.", style="bold red")
                aguardar(2)
        except requests.exceptions.RequestException:
            console.print("✖ Falha na conexão. Verifique a internet.", style="bold red")
            aguardar(2)

    while True:
        telefone = "".join(filter(str.isdigit, Prompt.ask("Telefone (11 dígitos)")))
        if len(telefone) == 11:
            break
        console.print("Número inválido, tente novamente.", style="bold red")

    while True:
        email = Prompt.ask("Email")
        if validar_email(email):
            if email_existe(email):
                console.print("❌ Email já cadastrado. Tente outro.", style="bold red")
                aguardar(2)
            else:
                break
        else:
            console.print("Email inválido.", style="bold red")

    while True:
        confirmar_email = Prompt.ask("Confirme seu email")
        if email == confirmar_email:
            break
        console.print("Emails diferentes, tente novamente.", style="bold red")

    while True:
        console.print("Senha deve conter 8+ caracteres, 1 letra e 1 número, sem caracteres especiais.", style="bold cyan")
        senha = Prompt.ask("Criar senha")
        resultado = validar_senha(senha)
        if resultado == "Aprovada!":
            break
        console.print(resultado, style="bold red")

    while True:
        confirmar_senha = Prompt.ask("Confirme sua senha")
        if senha == confirmar_senha:
            break
        console.print("Senhas diferentes, tente novamente.", style="bold red")

    end = endereco()

    while True:
        confirmar = int(Prompt.ask("\nConfirmar cadastro? [1] Sim [2] Não"))
        if confirmar == 1:
            pontos = carregar_pontos()
            pontos.append({
                "nome_ponto": nome_ponto,
                "cnpj": cnpj,
                "telefone": telefone,
                "email": email,
                "senha": senha,
                "endereco": end
            })
            salvar_pontos(pontos)
            console.print("✅ Cadastro de ponto efetuado!", style="bold green")
            aguardar(2)
            return
        elif confirmar == 2:
            if int(Prompt.ask("Deseja reiniciar? [1] Sim [2] Não")) == 1:
                cadastro_ponto()
            return

# ---------- FUNÇÃO PRINCIPAL DE CADASTRO ----------
def cadastro():
    limpar_tela()
    console.print("1 - Cadastro de usuário", style="bold cyan")
    console.print("2 - Cadastro de ponto", style="bold cyan")
    console.print("0 - Voltar", style="bold cyan")
    escolha = Prompt.ask("Escolha uma opção")
    
    if escolha == "1":
        cadastro_usuario()
    elif escolha == "2":
        cadastro_ponto()
    else:
        return

