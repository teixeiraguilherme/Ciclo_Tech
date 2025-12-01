import utils 
from rich.console import Console
from rich.prompt import Prompt

console = Console()

class Residuo:
    def __init__(self, nome, pontos_kg, co2_kg):
        self.nome = nome
        self.pontos_kg = pontos_kg
        self.co2_kg = co2_kg

    def calcular_pontos(self, peso):
        return peso * self.pontos_kg

    def calcular_impacto(self, peso):
        return peso * self.co2_kg


class Conta:
    def __init__(self, nome, email, senha, telefone, endereco):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco

    def definir_nova_senha(self, nova_senha):
        self.senha = nova_senha

class Usuario(Conta):
    def __init__(self, nome, email, senha, telefone, endereco, cpf, cidade, pontos=0, historico=None):
        super().__init__(nome, email, senha, telefone, endereco)
        self.cpf = cpf
        self.cidade = cidade
        self.pontos = pontos
        self.historico = historico if historico else []

    def adicionar_reciclagem(self, residuo_obj, peso):
        pts = residuo_obj.calcular_pontos(peso)
        impacto = residuo_obj.calcular_impacto(peso)
        self.pontos += pts
        
        self.historico.append({
            "material": residuo_obj.nome,
            "peso": peso,
            "pontos_ganhos": pts,
            "co2_evitado": impacto
        })
        return pts, impacto

    
    def editar_perfil_interativo(self, sistema):
        console.print("\n[yellow]--- MODO DE EDIÇÃO (Enter para manter atual) ---[/]")
        
        novo_nome = utils.solicitar_nome(self.nome)
        novo_email = utils.solicitar_email_cadastro(sistema, self.email) 
        novo_tel = utils.solicitar_telefone(self.telefone)
        novo_cpf = utils.solicitar_cpf(sistema, self.cpf)
        
        nova_cid = Prompt.ask(f"Cidade ({self.cidade})") or self.cidade
        
        if utils.confirmar_acao("Salvar alterações?"):
            utils.barra_progresso("Atualizando")
            self.nome = novo_nome
            self.email = novo_email
            self.telefone = novo_tel
            self.cpf = novo_cpf
            self.cidade = nova_cid
            
            sistema.salvar_dados()
            console.print("✅ Dados atualizados!", style="green")
            utils.aguardar(1)
        else:
            console.print("❌ Cancelado.", style="red")
            utils.aguardar(1)


    def to_dict(self):
        return {
            "nome": self.nome, "email": self.email, "senha": self.senha,
            "telefone": self.telefone, "endereco": self.endereco, 
            "cpf": self.cpf, "cidade": self.cidade,
            "pontos": self.pontos, "historico": self.historico
        }


class PontoColeta(Conta):
    def __init__(self, nome_ponto, email, senha, telefone, endereco, cnpj):
        super().__init__(nome_ponto, email, senha, telefone, endereco)
        self.nome_ponto = nome_ponto
        self.cnpj = cnpj

    def editar_perfil_interativo(self, sistema):
        console.print("\n[1] Editar Dados Básicos  [2] Editar Endereço")
        try:
            op = int(input("Opção: "))
        except ValueError:
            console.print("❌ Digite um número.", style="red"); utils.aguardar(1); return

        if op == 1:
            console.print("\n[yellow]--- DADOS BÁSICOS ---[/]")
            self.nome = utils.solicitar_nome(self.nome)
            self.email = utils.solicitar_email_cadastro(sistema, self.email)
            self.telefone = utils.solicitar_telefone(self.telefone)
            
            if utils.confirmar_acao("Salvar dados?"):
                sistema.salvar_dados()
                console.print("✅ Atualizado!", style="green")

        elif op == 2:
            console.print("\n[yellow]--- ENDEREÇO ---[/]")
            e = self.endereco
            rua = Prompt.ask(f"Rua ({e['rua']})") or e['rua']
            num = Prompt.ask(f"Num ({e['numero']})") or e['numero']
            bairro = Prompt.ask(f"Bairro ({e['bairro']})") or e['bairro']
            cidade = Prompt.ask(f"Cidade ({e['cidade']})") or e['cidade']
            
            if utils.confirmar_acao("Salvar endereço?"):
                self.endereco = {"rua": rua, "numero": num, "bairro": bairro, "cidade": cidade}
                sistema.salvar_dados()
                console.print("✅ Endereço atualizado!", style="green")
        
        utils.aguardar(1)


    def to_dict(self):
        return {
            "nome_ponto": self.nome, "email": self.email, "senha": self.senha,
            "telefone": self.telefone, "endereco": self.endereco, "cnpj": self.cnpj
        }