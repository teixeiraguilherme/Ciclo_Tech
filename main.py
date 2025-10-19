import menu_inicial
from utils import limpar_tela, aguardar
import tutorial
import login
import cadastro
import def_usuario
import def_ponto

while True:
    entrada = menu_inicial.menu_inicial()
    if entrada == 1: 
        limpar_tela()
        print("Chamando a função de tutorial...")
        aguardar(1)
        tutorial.tutorial()
    
    elif entrada == 2:
        limpar_tela()
        aguardar(1)
        print("Chamando a função de cadastro...")
        cadastro.cadastro()
    
    elif entrada == 3:
        tipo_usuario, usuario_logado = login.login() 
        if tipo_usuario == "usuario":
            while True:
                entrada_usuario = menu_inicial.menu_usuario(usuario_logado)
                if entrada_usuario == 1:
                    print("Chamando a função de procurar pontos de coleta...")
                    aguardar(1)
                    limpar_tela() 
                    def_usuario.procurar_pontos()
                elif entrada_usuario == 2:
                    #calcular_pontuacao()
                    print("Chamando a função de calcular pontuação...")
                elif entrada_usuario == 3:  
                    #impactos()
                    print("Chamando a função de impactos...")
                elif entrada_usuario == 4:
                    #indicacoes()
                    print("Chamando a função de indicações...")
                elif entrada_usuario == 5:
                    tutorial.tutorial()
                elif entrada_usuario == 6:
                    print("Chamando a função de perfil do usuário...")
                    aguardar(1)
                    limpar_tela()
                    entrada_perfil = def_usuario.perfil_usuario(usuario_logado)
                    if entrada_perfil == 1:
                        print("Chamando a função de editar perfil...")
                        def_usuario.editar_usuario(usuario_logado)
                    elif entrada_perfil == 2:
                        print("Chamando a função de excluir conta...")
                        confirmacao=def_usuario.excluir_usuario(usuario_logado)
                        if confirmacao == 1:
                            usuarios = cadastro.carregar_usuarios()
                            usuarios = [usuario for usuario in usuarios if usuario['email'] != usuario_logado['email']]
                            cadastro.salvar_usuarios(usuarios)
                            print("\n✅ Conta excluída com sucesso.")
                            menu_inicial.menu_inicial()
                            aguardar(2)
                        else:
                            print("\n❌ Ação cancelada. Sua conta não foi excluída.")
                            aguardar(2)
                    elif entrada_perfil == 3:
                        print("Chamando a função de redifinir senha...")
                        confirmacao = int(input("Tem certeza que deseja redefinir sua senha?[1] Sim [0] Não: "))
                        if confirmacao == 1:
                            login.esqueci_minha_senha()
                        else:
                            print("Retornando ao menu anterior.")
                            pass
                    elif entrada_perfil == 0:
                        print("Voltando ao menu anterior...")
                        aguardar(1)
                        limpar_tela()
                        continue
                    else:
                        print("\nDigite um número válido!\n")
                elif entrada_usuario == 0:
                    print("Saindo da conta...")
                    aguardar(2) 
                    break
                else: 
                    print("\nDigite um número válido!\n")

        elif tipo_usuario == "ponto":
            while True:
                entrada_ponto = menu_inicial.menu_ponto(usuario_logado)
                if entrada_ponto == 1:
                    #cadastrar_coletas()
                    print("Chamando a função de cadastrar coletas...")

                elif entrada_ponto == 2:
                    #impactos_ponto()
                    print("Chamando a função de impactos...")

                elif entrada_ponto == 3:
                    print("Chamando a função de perfil do ponto...")
                    aguardar(1)
                    limpar_tela()
                    entrada_perfil = def_ponto.perfil_ponto(usuario_logado)
                    if entrada_perfil == 1:
                        print("Chamando a função de editar perfil...")
                        def_ponto.editar_ponto(usuario_logado)
                    elif entrada_perfil == 3:
                        print("Chamando a função de excluir conta...")
                        confirmacao=def_ponto.excluir_ponto(usuario_logado)
                        if confirmacao == 1:
                            pontos = cadastro.carregar_pontos()
                            pontos = [ponto for ponto in pontos if ponto['email'] != usuario_logado['email']]
                            cadastro.salvar_pontos(pontos)
                            print("\n✅ Conta excluída com sucesso.")
                            menu_inicial.menu_inicial()
                            aguardar(2)
                        else:
                            print("\n❌ Ação cancelada. Sua conta não foi excluída.")
                            aguardar(2)
                    elif entrada_perfil == 4:
                        print("Chamando a função de redifinir senha...")
                        confirmacao = int(input("Tem certeza que deseja redefinir sua senha?[1] Sim [0] Não: "))
                        if confirmacao == 1:
                            login.esqueci_minha_senha()
                        else:
                            print("Retornando ao menu anterior.")
                            pass
            
                    elif entrada_perfil == 2:
                        print("Chamando a função de editar endereço...")
                        def_ponto.editar_endereco(usuario_logado)
                    elif entrada_perfil == 0:
                        print("Voltando ao menu anterior...")
                        aguardar(1)
                        limpar_tela()
                        continue

                elif entrada_ponto == 0:
                    break
                else:
                    print("\nDigite um número válido!\n")   

    elif entrada == 0:
        print("Menu fechado.")
        break 

    else:
        print("\nDigite um número válido!\n")
        aguardar(2)