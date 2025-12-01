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

    def atualizar_dados(self, nome, email, telefone, cpf, cidade):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.cidade = cidade

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

    def atualizar_dados(self, nome, email, telefone, endereco=None):
        self.nome_ponto = nome
        self.nome = nome 
        self.email = email
        self.telefone = telefone
        if endereco:
            self.endereco = endereco

    def to_dict(self):
        return {
            "nome_ponto": self.nome_ponto, "email": self.email, "senha": self.senha,
            "telefone": self.telefone, "endereco": self.endereco, "cnpj": self.cnpj
        }