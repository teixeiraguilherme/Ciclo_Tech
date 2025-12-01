<div align="center">
  <img width="500" height="624" alt="Image" src="https://github.com/user-attachments/assets/04c05592-b678-4213-9731-5d325bfe83bf" />
</div>
 



-----

<div align="center">
<h2> 🌳 Ciclotech: Recicle, Ganhe Pontos, Mova-se!</h2>
</div>


### 1\. Qual o objetivo do projeto?

O Ciclotech ataca dois grandes problemas urbanos: o **descarte incorreto de lixo** e o **fluxo trânsito**. O projeto nasceu para incentivar a reciclagem de forma prática e recompensadora, transformando um ato ambiental em um benefício financeiro real para o cidadão. Através de uma plataforma gamificada, nosso objetivo é engajar a comunidade, facilitar a conexão entre quem recicla e os pontos de coleta, e gerar dados de impacto que mostrem o poder da colaboração, como a quantidade de gás carbônico que foram evitados.

### 2\. Como o sistema funciona?

A plataforma conecta dois tipos de clientes:

  * **Usuário Comum:** O cidadão que separa seus resíduos.
  * **Ponto de Coleta:** Empresas e cooperativas parceiras que recebem os materiais.

O fluxo é simples:

1. **Cadastro e Localização:** O usuário se cadastra e encontra os pontos de coleta mais próximos.
2. **Registro da Reciclagem:** Ao levar o material, o Ponto de Coleta registra o tipo e o peso do resíduo, creditando os pontos automaticamente no perfil do usuário.
3. **Sistema de Pontos Inteligente:** O sistema de pontuação valoriza mais os materiais cujo descarte incorreto é mais prejudicial ao meio ambiente, como pilhas, lixo eletrônico e óleo de cozinha.
4. **Ranking e Impacto:** Os usuários podem acompanhar seu desempenho em um ranking municipal ou nacional e visualizar o impacto coletivo em tempo real, como o total de lixo reciclado e a quantidade de CO₂ evitada.
5. **Conversão em Benefício:** Ao atingir a pontuação necessária, o usuário pode converter seus pontos em créditos para o vale-transporte, fechando o ciclo de sustentabilidade e economia.

##

<h2>🖋️FUNCIONALIDADES PRIMEIRA RELEASE </h2>

<h4>RF001 - Menu inicial</h4> <p>Tela principal da aplicação, servindo como ponto de partida e hub de navegação para as demais funcionalidades centrais.</p>

<h4>RF002 - Cadastro usuário</h4> <p>Permite que novos usuários criem uma conta pessoal na plataforma, fornecendo dados básicos (como nome, e-mail e senha).</p>

<h4>RF003 - Cadastro ponto</h4> <p>Funcionalidade dedicada ao registro de novos pontos de coleta (cooperativas, ecopontos) no sistema, incluindo localização.</p>

<h4>RF004 - Login de usuário e ponto</h4> <p>Sistema de autenticação que permite o acesso seguro de usuários (que reciclam) e administradores de pontos (que recebem material) às suas respectivas contas.</p>

<h4>RF005 - Tutorial</h4> <p>Guia apresentado ao usuário, explicando como reciclar de maneira correta cada tipo de lixo.</p>

<h4>RF0010 - Procurar pontos</h4> <p>Ferramenta para exibir todos os pontos para o usuário localizar os pontos de coleta mais próximos de sua localização.</p>

<h4>RF012 - Perfil </h4> <p>Tela onde o usuário visualiza suas informações pessoais, pode editar e excluir.</p>

<h4>RF013 - Atualizar perfil </h4> <p>Permite ao usuário editar e salvar alterações em suas informações de cadastro (ex: mudar senha, mudar email, corrigir nome).</p>

<h2>🖋️FUNCIONALIDADES SEGUNDA RELEASE</h2>

<h4>RF006 - Ranking </h4> <p>Exibição de uma tabela de classificação (leaderboard) que posiciona os usuários com base em seu volume de reciclagem ou pontuação acumulada.</p>

<h4>RF007 - Impactos</h4> <p>Seção que exibe métricas e dados visuais sobre o impacto ambiental positivo gerado pelas ações de reciclagem do usuário (ex: CO2 evitado, água economizada).</p>

<h4>RF008 - Calculadora de conversão</h4> <p>Ferramenta utilitária para o usuário simular quanto seus recicláveis valem em pontos ou benefícios (ex: 5kg de plástico = X pontos).</p>

<h4>RF009 - Registro de reciclagem</h4> <p>Funcionalidade principal onde o ponto registra a entrega de materiais em um ponto de coleta, especificando tipo e quantidade (peso/volume).</p>

<h4>RF011 - Indicação</h4> <p>Funcionalidade informativa que indica ao usuário como converter seus pontos acumulados em benefícios (Vale Transporte). O sistema direciona o usuário para o local de troca e lista os documentos necessários para o resgate.</p>


<h2> ⚙️ LINGUAGEM E TECNOLOGIA </h2>

<h4>PYTHON 3.13.7</h4>

<br><h3>🧱 PARADIGMA E ESTRUTURA </h3>

- **Programação Orientada a Objetos (POO):** A base do projeto. O sistema utiliza Classes para representar Entidades (como `Usuario` e `PontoColeta`) que herdam características de uma classe mãe (`Conta`), garantindo encapsulamento e reutilização de código.

<br><h3>📚 BIBLIOTECAS </h3>

- 🎨 **Rich**: Responsável por toda a interface visual (CLI), criando painéis, tabelas, barras de progresso e estilização colorida no terminal.
- 🌐 **Requests:** Utilizada para consumir a BrasilAPI, permitindo o preenchimento automático de dados de empresas via CNPJ.
- 📧 **SMTPLib & Email**: Implementação do sistema de envio de e-mails reais para recuperação de senha e autenticação de dois fatores (2FA).
- 🔐 **Python-Dotenv**: Gerenciamento de variáveis de ambiente (`.env`) para proteger credenciais sensíveis (senha do e-mail empresarial).
- 💾 **JSON**: Utilizado como banco de dados local para persistência das informações de usuários, pontos de coleta e resíduos.
- 🎲 **Random**: Geração de códigos aleatórios de segurança para a validação de e-mail.
- 📂 **Pathlib & OS**: Manipulação segura de caminhos de arquivos, garantindo compatibilidade entre Windows e Linux.
  
<br><h3>💾 PERSISTÊNCIA DE DADOS </h3>

- **JSON (JavaScript Object Notation):** Utilizado como banco de dados local "serverless". O sistema lê e grava arquivos `.json` para manter o histórico de usuários, pontos de coleta e resíduos, permitindo que os dados persistam mesmo após fechar o programa.
  
----------------------------------------------------
<h3> 1.1 RELEASE </h3>

- **CAMADA DE SEGURANÇA -** Melhorias na  de redifinição de senha, acréscimo de verificação em duas etapas por email.  </p>
- **BUG 001 -** While inútil para sair da tela de tutorial, corrigido por pressione enter. </p>

----------------------------------------------------

## ▶️ Como Executar

1. **Requisitos**:
   - Python 3.10+
   - Biblioteca [requests](https://pypi.org/project/requests/)
   - Biblioteca [rich](https://pypi.org/project/rich/)
   - Biblioteca [dotenv](https://www.dotenv.org/)
2. **Instalação das dependências**:
   ```bash
   pip install requests
   ```
   ```bash
   pip install rich
   ```
   ```bash
   pip install python-dotenv
   ```


3. **Executar o jogo**:
   ```bash
   python main.py
   ```
---











