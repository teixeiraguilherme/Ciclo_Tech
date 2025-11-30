import json
import os
from models import Usuario, PontoColeta, Residuo

class BancoDeDados:
    def __init__(self):
        self.arquivos_usuarios = "usuarios.json"
        self.arquivos_pontos = "pontos.json"
        self.arquivos_residuos = "residuos.json"

    def _carregar_json(self, arquivo):
        if not os.path.exists(arquivo):
            return []
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                content = f.read()
                return json.loads(content) if content else []
        except:
            return []


    def _salvar_json(self, arquivo, dados):
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)


    def carregar_residuos(self):
        dados = self._carregar_json(self.arquivos_residuos)
        
        if not dados:
            dados_padrao = [
                {"nome": "Plastico", "pontos_kg": 10, "co2_kg": 1.5},
                {"nome": "Vidro", "pontos_kg": 5, "co2_kg": 0.3},
                {"nome": "Metal", "pontos_kg": 15, "co2_kg": 2.0},
                {"nome": "Papel", "pontos_kg": 5, "co2_kg": 0.8},
                {"nome": "Eletronico", "pontos_kg": 50, "co2_kg": 5.0},
                {"nome": "Oleo", "pontos_kg": 20, "co2_kg": 3.0},
                {"nome": "Organico", "pontos_kg": 15, "co2_kg": 0.7},
                {"nome": "Bateria", "pontos_kg": 70, "co2_kg": 4.0}
            ]
            self._salvar_json(self.arquivos_residuos, dados_padrao)
            dados = dados_padrao

        lista_residuos = []
        for d in dados:
            lista_residuos.append(Residuo(d['nome'], d['pontos_kg'], d['co2_kg']))
        return lista_residuos


    def carregar_usuarios(self):
        dados = self._carregar_json(self.arquivos_usuarios)
        lista = []
        for d in dados:
            user = Usuario(
                nome=d['nome'],
                email=d['email'],
                senha=d['senha'],
                telefone=d.get('telefone', ''),
                endereco=d.get('endereco', ''),
                cpf=d.get('cpf', ''),
                cidade=d.get('cidade', ''),
                pontos=d.get('pontos', 0),
                historico=d.get('historico', [])
            )
            lista.append(user)
        return lista


    def carregar_pontos(self):
        dados = self._carregar_json(self.arquivos_pontos)
        lista = []
        for d in dados:
            ponto = PontoColeta(
                nome_ponto=d['nome_ponto'],
                email=d['email'],
                senha=d['senha'],
                telefone=d.get('telefone', ''),
                endereco=d.get('endereco', {}),
                cnpj=d.get('cnpj', '')
            )
            lista.append(ponto)
        return lista


    def salvar_tudo(self, lista_usuarios, lista_pontos):
        dict_usuarios = [u.to_dict() for u in lista_usuarios]
        dict_pontos = [p.to_dict() for p in lista_pontos]
        
        self._salvar_json(self.arquivos_usuarios, dict_usuarios)
        self._salvar_json(self.arquivos_pontos, dict_pontos)