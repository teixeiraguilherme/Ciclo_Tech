from utils import limpar_tela, aguardar

def voltar_tutorial():
    while True:
        voltar = int(input("\nDeseja voltar ao menu tutorial? [1] Sim [2] Não: "))
        if voltar == 1:
            print("Voltando ao tutorial...")
            aguardar(2)
            return
        elif voltar == 2:
            print("") 
            
        else:
            print("Entrada inválida. Por favor, digite um número válido.")
            aguardar(2)

def tutorial():
    while True: 
        limpar_tela()
        print("_________BEM-VINDO AO TUTORIAL DE RECICLAGEM_________")
        print("\nAQUI VOCÊ VAI APRENDER A RECICLAR TODO E QUALQUER TIPO DE MATERIAL\n")
        print("      1 - Vidro")
        print("      2 - Plásticos")
        print("      3 - Papel e Papelão")
        print("      4 - Metais")
        print("      5 - Óleo de Cozinha")
        print("      6 - Baterias e Pilhas")
        print("      7 - Lixo Eletrônico")
        print("      8 - Lixo Orgânico")
        print("      9 - Voltar Menu")
        
        try:
            number_tutorial = int(input("\nSelecione o material desejado: "))

            if number_tutorial == 1:
                aguardar(3)
                limpar_tela()
                print("\nComo preparar: Lave para remover todos os resíduos. \n Não é necessário remover os rótulos. Se algo quebrar, embale \n os cacos em jornal grosso ou em uma caixa de papelão para \n proteger os coletores de acidentes. ")
                voltar_tutorial()
            elif number_tutorial == 2:
                aguardar(3)
                limpar_tela()
                print("\nComo preparar: Lave-os com água de reúso (da louça, por exemplo) \n para remover restos de comida ou bebida. Isso evita o mau cheiro \n e a atração de animais. Amassar as garrafas economiza um espaço valioso no transporte.")
                voltar_tutorial()
            elif number_tutorial == 3:
                aguardar(3)
                limpar_tela()
                print("\nComo preparar: Certifique-se de que não estejam sujos \n com gordura ou restos de comida (guardanapos sujos e caixas \n de pizza engorduradas não são recicláveis). Desmonte as caixas \n para otimizar o espaço.")
                voltar_tutorial()
            elif number_tutorial == 4:
                aguardar(3)
                limpar_tela()
                print("\nComo preparar: Lave latas de alimentos (atum, milho) \n para tirar os resíduos. Amassar as latinhas de alumínio facilita \n muito o armazenamento e o transporte.")
                voltar_tutorial()
            elif number_tutorial == 5:
                aguardar(3)
                limpar_tela()
                print("\nComo descartar: Após usar, espere o óleo esfriar completamente. \n Use um funil para despejá-lo em uma garrafa PET e feche bem. Acumule e leve \n a um ponto de coleta especializado.")
                voltar_tutorial()
            elif number_tutorial == 6:
                aguardar(3)
                limpar_tela()
                print("\nComo descartar: Guarde-as em um recipiente plástico fechado, separado \n dos outros lixos. Leve a um dos muitos pontos de coleta disponíveis em supermercados, \n farmácias e lojas de eletrônicos.")
                voltar_tutorial()
            elif number_tutorial == 7:
                aguardar(3)
                limpar_tela()
                print("\nComo descartar: Procure por Ecopontos ou locais \n de descarte específicos para lixo eletrônico em sua cidade. \n Muitas lojas de telefonia e eletrônicos também possuem programas de coleta.")
                voltar_tutorial()
            elif number_tutorial == 8:
                aguardar(3)
                limpar_tela()
                print("\nComo preparar: Separe cascas de frutas, legumes, verduras, borra \n de café e cascas de ovos. Evite colocar carnes, laticínios e alimentos \n gordurosos em excesso na sua composteira caseira.")
                voltar_tutorial()
            elif number_tutorial == 9:
                print("\n Voltando ao menu...")
                aguardar(3)
                return
            else:
                print("Digite um número válido")
                aguardar(2)
        except ValueError:
            print("Erro, digite um número válido!")
            aguardar(2)
