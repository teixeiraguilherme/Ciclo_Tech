from utils import limpar_tela, aguardar

def menu_ponto(nome_ponto):
    
    while True:
        limpar_tela()
        print(f"--- 🏢 PAINEL DO PONTO ---")
        print(f"Bem-vindo(a), {nome_ponto}!")
        
        print("\n1. Gerenciar itens")
        print("2. Adicionar novo item")
        print("0. Sair (Voltar ao menu principal)")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            print("Chamando a função de gerenciar itens...")
            aguardar(2)

        elif opcao == '0':
            print("\nDeslogando...")
            aguardar(1)
            break

        else:
            print("Opção inválida!")
            aguardar(1)