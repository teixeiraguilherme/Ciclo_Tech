from utils import limpar_tela, aguardar
from rich.console import Console

console = Console()

def tutorial():
    while True: 
        limpar_tela()
        console.print(f"--- 🗑️ BEM-VINDO AO TUTORIAL DE RECICLAGEM ---\n", style="bold cyan")
        console.print("AQUI VOCÊ VAI APRENDER A RECICLAR TODO E QUALQUER TIPO DE MATERIAL\n", style="bold green")
        print("      1 - Vidro")
        print("      2 - Plásticos")
        print("      3 - Papel e Papelão")
        print("      4 - Metais")
        print("      5 - Óleo de Cozinha")
        print("      6 - Baterias e Pilhas")
        print("      7 - Lixo Eletrônico")
        print("      8 - Lixo Orgânico")
        print("      0 - Voltar Menu")
        
        try:
           
            entrada = input("\nSelecione o material desejado: ")
            if not entrada.isdigit():
                print("Digite apenas números.")
                aguardar(1)
                continue
                
            op = int(entrada)
            
            msg = ""
            if op == 1: msg = "Vidro: Lave para remover todos os resíduos. \n Não é necessário remover os rótulos. Se algo quebrar, embale \n os cacos em jornal grosso ou em uma caixa de papelão para \n proteger os coletores de acidentes."
            elif op == 2: msg = "Plástico: Lave-os com água de reúso (da louça, por exemplo) \n para remover restos de comida ou bebida. Isso evita o mau cheiro \n e a atração de animais. Amassar as garrafas economiza um espaço valioso no transporte."
            elif op == 3: msg = "Papel: Certifique-se de que não estejam sujos \n com gordura ou restos de comida (guardanapos sujos e caixas \n de pizza engorduradas não são recicláveis). Desmonte as caixas \n para otimizar o espaço."
            elif op == 4: msg = "Metal: Lave latas de alimentos (atum, milho) \n para tirar os resíduos. Amassar as latinhas de alumínio facilita \n muito o armazenamento e o transporte."
            elif op == 5: msg = "Óleo: Após usar, espere o óleo esfriar completamente. \n Use um funil para despejá-lo em uma garrafa PET e feche bem. Acumule e leve \n a um ponto de coleta especializado."
            elif op == 6: msg = "Pilhas: Guarde-as em um recipiente plástico fechado, separado \n dos outros lixos. Leve a um dos muitos pontos de coleta disponíveis em supermercados, \n farmácias e lojas de eletrônicos."
            elif op == 7: msg = "Eletrônico: Procure por Ecopontos ou locais \n de descarte específicos para lixo eletrônico em sua cidade. \n Muitas lojas de telefonia e eletrônicos também possuem programas de coleta."
            elif op == 8: msg = "Orgânico: Separe cascas de frutas, legumes, verduras, borra \n de café e cascas de ovos. Evite colocar carnes, laticínios e alimentos \n gordurosos em excesso na sua composteira caseira."
            elif op == 0: return 
            else:
                print("Opção inválida.")
                aguardar(1)
                continue
            
            if msg:
                limpar_tela()
                console.print("--- COMO DESCARTAR ---", style="bold yellow")
                console.print(msg)
                input("\n[Enter] para voltar...")
                
        except ValueError:
            print("Opção inválida.")
            aguardar(1)
