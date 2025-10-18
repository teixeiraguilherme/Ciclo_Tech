from utils import limpar_tela, aguardar

def menu_usuario(nome_usuario):
    
    while True:
        limpar_tela()
        print(f"--- 👤 PAINEL DO USUÁRIO ---")
        print(f"Bem-vindo(a), {nome_usuario}!") 
        
        print("\n1. Encontrar pontos de coleta")
        print("2. Agendar coleta")
        print("3. Meu perfil")
        print("0. Sair (Voltar ao menu principal)")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            print("Chamando a função de procurar pontos...")
            aguardar(2)
        
        elif opcao == '2':
            print("Chamando a função de agendamento...")
            aguardar(2)
            
        elif opcao == '0':
            print("\nDeslogando...")
            aguardar(1)
            break 
        
        else:
            print("Opção inválida!")
            aguardar(1)