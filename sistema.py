import utils
from database import BancoDeDados
from models import Usuario, PontoColeta
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

console = Console()

class SistemaCiclotech:
    def __init__(self):
        self.banco = BancoDeDados()
        self.usuarios = self.banco.carregar_usuarios()
        self.pontos_coleta = self.banco.carregar_pontos()
        self.residuos = self.banco.carregar_residuos()

    def salvar_dados(self):
        self.banco.salvar_tudo(self.usuarios, self.pontos_coleta)

    ''' LÓGICA DE NEGÓCIO (BACKEND) '''

    def login(self, email, senha):
        for u in self.usuarios:
            if u.email == email and u.senha == senha: return "usuario", u
        for p in self.pontos_coleta:
            if p.email == email and p.senha == senha: return "ponto", p
        return None, None


    def email_existe(self, email):
        todos = self.usuarios + self.pontos_coleta
        for conta in todos:
            if conta.email == email: return True
        return False


    def cpf_existe(self, cpf):
        for u in self.usuarios:
            if u.cpf == cpf: return True
        return False


    def cnpj_existe(self, cnpj):
        for p in self.pontos_coleta:
            if p.cnpj == cnpj: return True
        return False


    def redefinir_senha(self, email, nova_senha):
        conta = next((u for u in self.usuarios if u.email == email), None)
        if not conta:
            conta = next((p for p in self.pontos_coleta if p.email == email), None)
        
        if conta:
            conta.senha = nova_senha
            self.salvar_dados()
            return True, "Senha atualizada com sucesso!"
        return False, "Email não encontrado."


    def cadastrar_usuario(self, nome, email, senha, telefone, cidade, cpf):
        
        if self.email_existe(email): return False
        if self.cpf_existe(cpf): return False
        
        novo = Usuario(nome, email, senha, telefone, cidade, cpf, cidade)
        self.usuarios.append(novo)
        self.salvar_dados()
        return True


    def cadastrar_ponto(self, nome, email, senha, telefone, endereco, cnpj):
        if self.email_existe(email): return False
        if self.cnpj_existe(cnpj): return False 
        
        novo = PontoColeta(nome, email, senha, telefone, endereco, cnpj)
        self.pontos_coleta.append(novo)
        self.salvar_dados()
        return True


    def gerar_ranking(self):
        return sorted(self.usuarios, key=lambda x: x.pontos, reverse=True)


    def obter_residuo_por_numero(self, numero):
        try:
            indice = int(numero)
            if 0 <= indice < len(self.residuos):
                return self.residuos[indice]
            else:
                return None
        except (ValueError, TypeError):
            return None


    def processar_reciclagem(self, email_usuario, numero_material, peso):
        cliente = next((u for u in self.usuarios if u.email == email_usuario), None)
        if not cliente: return False, "Usuário não encontrado."

        residuo = self.obter_residuo_por_numero(numero_material)
        if not residuo: 
            return False, "Material inválido. Verifique o número na lista acima."

        pts, imp = cliente.adicionar_reciclagem(residuo, peso)
        self.salvar_dados()
        return True, f"Creditado {pts:.2f} pts para {cliente.nome} por {peso:.2f}kg de {residuo.nome}."


    def simular_conversao(self, numero_material, peso):
        res = self.obter_residuo_por_numero(numero_material)
        if res: return res.calcular_pontos(peso)
        return 0
    
    
    '''MÉTODOS DE INTERFACE (FRONTEND) - CHAMADOS PELO MAIN''' 
   

    def interface_login(self):
        while True:
            utils.limpar_tela()
            console.print(Panel("🔐 [bold white]ACESSO AO SISTEMA[/]", style="bold green", expand=False))
            
            console.print("\n[bold]Escolha uma opção:[/]")
            console.print("[1] 👤 Entrar na minha conta")
            console.print("[2] 🔑 Esqueci minha senha")
            console.print("[Enter] para voltar...")
            
            opcao = input("\nOpção: ").strip()
            
            if not opcao or opcao == "0":
                return None, None

            elif opcao == "1":
                console.print("\n--- 🔐 CREDENCIAIS ---", style="yellow")
                email = Prompt.ask("Email")
                senha = Prompt.ask("Senha")
                
                utils.barra_progresso("Autenticando", 1.0)
                tipo, obj = self.login(email, senha)
                    
                if not obj:
                    console.print("❌ Email ou senha incorretos.", style="bold red")
                    utils.aguardar(2)
                    continue 
                return tipo, obj

            elif opcao == "2":
                self.interface_esqueci_senha()
                
            
            else:
                console.print("❌ Opção inválida.", style="red")
                utils.aguardar(1)


    def interface_cadastro_usuario(self):
        console.print("--- NOVO USUÁRIO ---", style="cyan")
        nome = utils.solicitar_nome()
        email = utils.solicitar_email_cadastro(self)
        senha = utils.solicitar_senha_segura()
        tel = utils.solicitar_telefone()
        cpf = utils.solicitar_cpf(self) 
        cidade = Prompt.ask("Cidade")

        if utils.confirmar_acao("Confirmar cadastro?"):
            utils.barra_progresso("Salvando")
            self.cadastrar_usuario(nome, email, senha, tel, cidade, cpf)
            console.print("✅ Usuário cadastrado com sucesso!", style="bold green")
        else:
            console.print("Cancelado.", style="red")
        utils.aguardar(2)


    def interface_cadastro_ponto(self):
        console.print("--- NOVO PONTO DE COLETA ---", style="magenta")
        
        sucesso, api = utils.consultar_cnpj_api(self) 
        if not sucesso: return

        nome = Prompt.ask("Nome Fantasia", default=api['nome'])
        email = utils.solicitar_email_cadastro(self, api['email'])
        senha = utils.solicitar_senha_segura()
        
        tel_padrao = utils.limpar_apenas_numeros(api['telefone'])
        tel_padrao = tel_padrao if len(tel_padrao) == 11 else ""
        tel = utils.solicitar_telefone(tel_padrao)

        console.print("\n[yellow]Endereço[/]")
        rua = Prompt.ask("Rua", default=api['logradouro'])
        num = Prompt.ask("Número", default=api['numero'])
        bairro = Prompt.ask("Bairro", default=api['bairro'])
        cidade = Prompt.ask("Cidade", default=api['municipio'])
        endereco = {"rua": rua, "numero": num, "bairro": bairro, "cidade": cidade}

        if utils.confirmar_acao("Salvar Ponto?"):
            utils.barra_progresso("Salvando")
            if self.cadastrar_ponto(nome, email, senha, tel, endereco, api['cnpj_limpo']):
                console.print("✅ Ponto cadastrado!", style="green")
            else:
                console.print("❌ Erro: CNPJ ou Email já cadastrado.", style="bold red")
        utils.aguardar(2)


    def interface_registrar_reciclagem(self):
        utils.limpar_tela()
        console.print("\n--- Materiais Disponíveis ---", style="bold yellow")
        for i, r in enumerate(self.residuos): 
            console.print(f"[{i}] {r.nome}")
        console.print("---------------------------")
        
        email = input("Email do Cliente: ")
        

        try:
            mat_input = input("Número do Material: ")
            mat_num = int(mat_input)

            if mat_num < 0 or mat_num >= len(self.residuos):
                raise ValueError
        except ValueError:
            console.print("❌ Material inválido! Escolha o número da lista.", style="red")
            utils.aguardar(2)
            return 

        
        peso_final = 0.0
        while True:
            
            peso_str = input("Peso (kg): ")
            try:
                peso_final = float(peso_str.replace(',', '.'))
                
                if peso_final <= 0:
                    console.print("❌ O peso deve ser maior que zero.", style="red")
                    continue
                break 
            except ValueError:
                console.print("❌ Peso inválido! Digite apenas números.", style="red")

       
        try:
            ok, msg = self.processar_reciclagem(email, mat_num, peso_final)
            console.print(msg, style="green" if ok else "red")
        except Exception as e:
            console.print(f"❌ Erro interno: {e}", style="bold red")
        
        utils.aguardar(4)


    def interface_esqueci_senha(self):
        console.print("[yellow]RECUPERAÇÃO DE SENHA[/]", justify="center")
        email = Prompt.ask("Email da conta")
        
        if not self.email_existe(email):
            console.print("❌ Email não encontrado.", style="red"); utils.aguardar(2); return

        cod = utils.gerar_codigo_verificacao()
        console.print(f"\nCódigo de segurança: [bold cyan]{cod}[/]")
        
        if input("Digite o código: ") != str(cod):
            console.print("❌ Código errado.", style="red"); utils.aguardar(2); return
            
        nova = utils.solicitar_senha_segura()
        utils.barra_progresso("Atualizando")
        self.redefinir_senha(email, nova)
        console.print("✅ Senha redefinida!", style="green"); utils.aguardar(2)


    def interface_impactos(self, usuario_logado):
        utils.limpar_tela()
        console.print("--- 🌍 DASHBOARD DE SUSTENTABILIDADE ---", style="bold green", justify="center")

        total_usuarios = len(self.usuarios)
        
        peso_global_total = 0.0
        co2_global_total = 0.0 

        for u in self.usuarios:
            for item in u.historico:
                
                peso_global_total += item.get('peso', 0)
                
                co2_global_total += item.get('co2_evitado', 0)

        grid_global = Table.grid(padding=2)
        grid_global.add_column(justify="center", style="bold white")
        grid_global.add_column(justify="center", style="bold yellow")
        grid_global.add_column(justify="center", style="bold green")

        grid_global.add_row("👥 Usuários", "⚖️ Lixo Reciclado", "💨 CO2 Evitado")
        grid_global.add_row(
            f"{total_usuarios}", 
            f"{peso_global_total:.2f} kg", 
            f"{co2_global_total:.2f} kg" 
        )

        console.print(Panel(
            Align.center(grid_global), 
            title="🌎 IMPACTO COLETIVO (Ciclotech Global)", 
            border_style="green"
        ))

     
        if not usuario_logado.historico:
            console.print("\n[italic gray]Você ainda não contribuiu para esses números. Comece hoje![/]", justify="center")
        else:
            meu_peso = sum(item.get('peso', 0) for item in usuario_logado.historico)
            meu_co2 = sum(item.get('co2_evitado', 0) for item in usuario_logado.historico)
            
            arvores = meu_co2 / 22  
            
            texto_pessoal = (
                f"\n👤 [bold cyan]{usuario_logado.nome}[/], sua parte nessa história:\n\n"
                f"📦 Você reciclou: [bold white]{meu_peso:.2f} kg[/]\n"
                f"💨 Você evitou:   [bold green]{meu_co2:.2f} kg[/] de CO2\n\n"
                f"🌳 Isso equivale a [bold green]{arvores:.2f} árvores[/] trabalhando pelo planeta!"
            )
            
            console.print(Panel(texto_pessoal, title="👤 SEU IMPACTO PESSOAL", border_style="cyan"))

        input("\nPressione Enter para voltar...")


    def interface_calculadora(self):
        utils.limpar_tela()
        console.print("--- 🧮 CALCULADORA CICLOTECH ---", style="bold cyan")
        
        console.print("\nO que você deseja simular?", style="yellow")
        console.print("[1] ♻️ PONTOS")
        console.print("[2] 💰 CRÉDITOS (R$)")
        
        try:
            modo = int(input("\nOpção: "))
        except ValueError:
            return
        
        if modo == 1:
            utils.limpar_tela()
            console.print("--- ♻️ SIMULADOR DE PONTOS ---", style="bold green")
            
            console.print("\nSelecione o material:", style="yellow")
            for i, r in enumerate(self.residuos): 
                console.print(f"[{i}] {r.nome} (Vale {r.pontos_kg} pts/kg)")
            
            try:
                op = int(input("\nDigite o número do material: "))
                material_escolhido = self.residuos[op]
            except (ValueError, IndexError):
                console.print("❌ Material inválido!", style="red"); utils.aguardar(2); return

            peso = 0.0
            while True:
                try:
                    entrada = input("Quantos Kg você tem? ")
                    peso = float(entrada.replace(',', '.'))
                    if peso <= 0:
                        console.print("❌ O peso deve ser maior que zero.", style="red"); continue
                    break
                except ValueError:
                    console.print("❌ Digite um número válido.", style="red")

            pontos = material_escolhido.calcular_pontos(peso)
            co2 = material_escolhido.calcular_impacto(peso)

            console.print("\n---------------- RESULTADO ----------------", style="bold white")
            console.print(f"📦 Material: [cyan]{material_escolhido.nome}[/]")
            console.print(f"⚖️ Peso:     [cyan]{peso} kg[/]")
            console.print(f"💎 Pontos:   [bold yellow]{pontos:.2f}[/]")
            console.print("-------------------------------------------")

        elif modo == 2:
            utils.limpar_tela()
            console.print("--- 💰 CONVERSOR DE CRÉDITOS ---", style="bold yellow")
        
            TAXA_CONVERSAO = 0.40
            
            while True:
                try:
                    entrada = input("\nQuantos pontos você quer converter? ")
                    pontos_input = float(entrada.replace(',', '.'))
                    if pontos_input < 0:
                        console.print("❌ Valor não pode ser negativo.", style="red"); continue
                    break
                except ValueError:
                    console.print("❌ Digite um número válido.", style="red")
            
            creditos = pontos_input * TAXA_CONVERSAO
            
            console.print("\n---------------- RESULTADO ----------------", style="bold white")
            console.print(f"💎 Pontos inseridos: [yellow]{pontos_input:.2f}[/]")
            console.print(f"💵 Créditos gerados: [bold green]R$ {creditos:.2f}[/]")
            console.print("-------------------------------------------")

        else:
            console.print("❌ Opção inválida.", style="red")
        
        input("\nPressione Enter para voltar...")
    

    def interface_trocar_senha_logado(self, usuario):
        console.print("\n[bold yellow]ALTERAR SENHA[/]")
        atual = Prompt.ask("Digite sua senha atual", password=True)
        
        if atual != usuario.senha:
            console.print("❌ Senha atual incorreta!", style="bold red")
            utils.aguardar(2); return

        console.print("Digite a nova senha:")
        nova = utils.solicitar_senha_segura()
        
        if utils.confirmar_acao("Tem certeza?"):
            usuario.senha = nova
            self.salvar_dados()
            console.print("✅ Senha alterada!", style="bold green")
        utils.aguardar(2)


    def interface_encontrar_pontos(self):
        utils.limpar_tela()
        console.print("--- 📍 PONTOS DE COLETA DISPONÍVEIS ---", style="bold green", justify="center")
        
        if not self.pontos_coleta:
            console.print("\n[italic yellow]Nenhum ponto cadastrado ainda.[/]", justify="center")
            utils.aguardar(3)
            return

        tabela = Table(show_header=True, header_style="bold cyan", expand=True, border_style="green", show_lines=True)
        
        tabela.add_column("Nome do Ponto", style="bold white", justify="center", vertical="middle")
        tabela.add_column("Endereço Completo", style="white")
        tabela.add_column("Contato", justify="center", vertical="middle")

        for p in self.pontos_coleta:
            end = p.endereco
            
            if isinstance(end, dict):
                rua = end.get('rua', 'Rua não informada')
                num = end.get('numero', 'S/N')
                bairro = end.get('bairro', 'Bairro não inf.')
                cidade = end.get('cidade', 'Cidade não inf.')
                
                endereco_visual = (
                    f"🏠 {rua}, {num}\n"
                    f"[italic gray]{bairro}[/]\n"
                    f"[bold cyan]{cidade}[/]"
                )
            else:
                endereco_visual = str(end) 

            tabela.add_row(
                f"[bold yellow]{p.nome_ponto}[/]",
                endereco_visual,                    
                f"📞 {p.telefone}"                  
            )

        console.print(tabela)
        input("\nPressione Enter para voltar...")