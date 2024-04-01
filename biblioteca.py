from FuncoesEBibliotecas import *
from Classes import *
LimparTerminal()

SENHAS = ["Provisório"]
FUNCIONARIO = []
CaracteristicasFUNCIONARIO = []
lista_livro = [0]
lista_revista = [0]
lista_jornal = [0]
lista_funcionario = [0]
lista_cliente = [0]
funcionarios = []
caracter = []
adm = False
Login = False
id_funcionario = 0
id_livro=0
id_jornal=0
id_revista=0
while True:
    SENHAS[0] = Criptografar(input("Seja bem vindo ao Sistema da Biblioteca.\nInsira uma senha para a conta de Administrador, que tem ID 0: "))
    LimparTerminal()
    if (Criptografar(input("Repita a senha: ")) == SENHAS[0]):
        print("Senha validada com sucesso!")
        break
    else:
        print("Senhas não conferem.")
        time.sleep(0.5)
    LimparTerminal()

LimparTerminal()
Pergunta = Criptografar(input("Insira uma frase de segurança (Esse texto será utilizada para recuperar a sua senha caso você esqueça-a): "))
LimparTerminal()
confer = Admin(0,SENHAS[0],Pergunta)


while True: #Loop do programa. 
    # Tela de Login
    LimparTerminal()
    while not Login:
        LimparTerminal()
        ID = EntradaInteiraMaiorIgualQueZero("Digite o seu ID: ")
        LimparTerminal()
        if ID == 0:
            #Pessoa está tentando logar no perfil de adm
                LimparTerminal()
                if (Criptografar(input("Digite sua senha: ")) == SENHAS[0]):
                    LimparTerminal()
                    print("Acesso Liberado.")
                    adm = True
                    Login = True
                    LimparTerminal()
                else:
                    LimparTerminal()
                    if (input("Senha incorreta.\n\nSe deseja redefinir a senha digite 1. Se não, apenas pressione enter para voltar ao início: ") == '1'):
                        for j in range(3, 0, -1):
                            LimparTerminal()
                            if (Criptografar(input("Digite a Frase de Segurança: ")) == Pergunta):
                                SENHAS[0] = Criptografar(input("Redefina sua senha: "))
                                LimparTerminal()
                                break
                            else:
                                print(f"Tente novamente (Restam {j-1} tentativas)")
                            LimparTerminal()
                    LimparTerminal()

        elif (ID < len(SENHAS) and (ID > 0)):
            LimparTerminal()
            if (Criptografar(input("Digite sua senha: ")) == SENHAS[ID]):
                print("Acesso Liberado ",lista_funcionario[ID][1],".") #Podemos adicionar uma variável {nome[ID]} e colocarmos algo como "Acesso Liberado Pedro"
                Login = True
                #LimparTerminal()
            else:
                print("Acesso Negado.")
        else:
            print("ID não existe") 
            time.sleep(1)   
        
    LimparTerminal()        
    if adm: 
        while True:
            LimparTerminal()        
            Decisao = EntradaInteiraMaiorIgualQueZero("Escolha o que deseja fazer:\n1 - Editar Informações dos Funcionários\n2 - Opções sobre Livros, Jornais e Revistas\n3 - Editar Informações dos Clientes\n0 - SAIR\n")
            LimparTerminal()
            if (Decisao == 1):
                if (len(SENHAS) == 1):
                    if (input(("Não existem funcionários no sistema. Deseja adicionar agora (S/N)? ")).lower() == "s"):
                        contadorfuncionarionovo=0
                        while contadorfuncionarionovo==0:
                            id_funcionario = id_funcionario+1
                            funcionarios=Funcionario(input("Digite o nome do funcionario que você irá adicionar: \n"),input("Digite o cpf do novo funcionário:"),input("Digite o email do novo funcionário: \n"),input("Digite o telefone do novo funcionário: \n"),(input("Digite o endereço: ")),lista_funcionario,id_funcionario,input("Digite a senha do login do novo funcionário: \n"),input("digite o salário: \n"),input("Quantas horas ele deverá trabalhar mensalmente: \n"))
                            print(funcionarios.exibir_info_pessoa())
                            abc=input("As informações do novo funcionário estão corretas?S/N\n").lower()
                            if abc=="s":
                                contadorfuncionarionovo=1
                                print("O id do novo funcionário é",lista_funcionario[id_funcionario][5],":")
                            else:
                                id_funcionario = id_funcionario-1
                        #FUNCIONARIO.append(lista_funcionario) nn precisa mais disso pq o lista_funcionario ja faz essa função
                        funcionarios = [] #Resetar a lista pro próximo uso
                        ID = len(SENHAS) 
                        VerificarSenhas(SENHAS, f"Insira a senha do funcionário de ID {ID} para revisão: ", ID)
                        LimparTerminal()
                    else:
                        print("Ok, voltando o sistema.\nErrar é humano.")
                        Login = False
                        adm = False
                        break  
                elif(len(SENHAS)>=2):
                    xyz=EntradaInteiraMaiorIgualQueZero("Escolha o que deseja fazer sobre os funcionários:\n1 - Adicionar funcionário\n2 - Excluir algum funcionário\n3 - Editar Informações dos funcionários\n0 - SAIR\n") 
                    if xyz==1:
                        contadorfuncionarionovo=0
                        while contadorfuncionarionovo==0:
                            id_funcionario = id_funcionario+1
                            funcionarios=Funcionario(input("Digite o nome do funcionario que você irá adicionar: \n"),input("Digite o cpf do novo funcionário:"),input("Digite o email do novo funcionário: \n"),input("Digite o telefone do novo funcionário: \n"),(input("Digite o endereço: ")),lista_funcionario,id_funcionario,input("Digite a senha do login do novo funcionário: \n"),input("digite o salário: \n"),input("Quantas horas ele deverá trabalhar mensalmente: \n"))
                            print(funcionarios.exibir_info_pessoa())
                            abc=input("As informações do novo funcionário estão corretas?S/N\n").lower()
                            if abc=="s":
                                contadorfuncionarionovo=1
                            else:
                                id_funcionario = id_funcionario-1
                        #FUNCIONARIO.append(lista_funcionario) nn precisa mais disso pq o lista_funcionario ja faz essa função
                        funcionarios = [] #Resetar a lista pro próximo uso
                        ID = len(SENHAS) 
                        VerificarSenhas(SENHAS, f"Insira a senha do funcionário de ID {ID} para revisão: ", ID)
                        LimparTerminal()
                    elif xyz==0:
                        Login = False
                        adm = False
                        break
            elif(Decisao==2):
                tipo=EntradaInteiraMaiorIgualQueZero("Escolha qual tipo você quer: \n1-Livros\n2-Jornal\n3-Revistas\n0-Sair\n")
                if tipo==1:
                    LimparTerminal()           
                    decisao=EntradaInteiraMaiorIgualQueZero("Você escolheu a opção sobre Livros:\nO que deseja fazer 1-Adicionar Livros 2-Excluir Livros 3-Mudar informações dos livros 4-empréstimo de Livros 0-Sair \n ")
                    if (len(lista_livro)==1 and decisao!=1):
                        decisao_imp=input("Não tem nenhum Livro ainda, deseja adiocionar agora: S/N \n Se a resposta for não você irá deslogar por conta de erro humano: ").lower()
                        if decisao_imp== "s":    
                            decisao=1
                        else:
                            print("Ok, voltando o sistema.\nErrar é humano.")
                            Login = False
                            adm = False
                            break
                    if decisao==1:
                        contadorlivronovo=0
                        while contadorlivronovo==0:
                            id_livro=id_livro+1
                            livro=Livro(input("Digite o titulo do novo livro: "),id_livro,input("Digite a editora do livro:"),'L',input("Digite a quantidade de cópias desse livro que você irá adicionar: "),lista_livro,input("Digite o ano de publicação do livro: "),input("Digite a edição do livro: "),input("Digite o autor do livro: "))
                            print(livro.exibir())
                            #(input("As informações do novo livro estão corretas?S/N\n")).lower()
                            if input("As informações do novo livro estão corretas?S/N\n").lower()=="s":
                                contadorlivronovo=1
                            else:
                                id_livro = id_livro-1
                    #elif decisao==2:
                       
                    #elif decisao==3:
                        
                    #elif decisao==4:
                        
                    else:
                        Login = False
                        adm = False
                        break
                elif tipo==2:
                    LimparTerminal()
                    decisao=EntradaInteiraMaiorIgualQueZero("Você escolheu a opção sobre Jornais:\nO que deseja fazer 1-Adicionar Jornais 2-Excluir Jornais 3-Mudar informações dos Jornais 4-empréstimo de jornais 0-Sair ")
                    if decisao==1:
                        if (len(lista_jornal)==1 and decisao!=1):
                            decisao_imp=input("Não tem nenhum jornal ainda, deseja adiocionar agora: S/N\nSe a resposta for não você irá deslogar por conta de erro humano:\n").lower()
                            if decisao_imp== "s":    
                                decisao=1
                            else:
                                print("Ok, voltando o sistema.\nErrar é humano.")
                                Login = False
                                adm = False
                                break
                        contadorjornalnovo=0
                        while contadorjornalnovo==0:
                            id_jornal=id_jornal+1
                            nome_jornal=input("Digite o titulo do novo jornal: ") 
                            jornal=Jornal(nome_jornal,id_jornal,input("Digite a editora do jornal: "),'J',lista_jornal,input("Digite a data de publicação do jornal: "),input("Digite a quantidade de cópias do jornal que você irá adicionar: "))
                            print(jornal.exibir())
                            ac=input("As informações do novo jornal estão corretas?S/N\n").lower()
                            if ac=="s":
                                contadorjornalnovo=1
                            else:
                                id_jornal = id_jornal-1
                    #elif decisao==2:
                        
                    #elif decisao==3:
                        
                    #elif decisao==4:
                        
                    else:
                        Login = False
                        adm = False
                        break
                elif tipo==3:
                    decisao=EntradaInteiraMaiorIgualQueZero("Você escolheu a opção sobre Revistas:\nO que deseja fazer 1-Adicionar Revistas 2-Excluir Revistas 3-Mudar informações dos Jornais 4-empréstimo de Jornais 0-Sair ")
                    if (len(lista_revista)==1 and decisao!=1):
                        decisao_imp=input("Não tem nenhuma revista ainda, deseja adiocionar agora: S/N\nSe a resposta for não você irá deslogar por conta de erro humano:\n").lower()
                        if decisao_imp== "s":    
                            decisao=1
                        else:
                            print("Ok, voltando o sistema.\nErrar é humano.")
                            Login = False
                            adm = False
                            break
                    if decisao==1:
                        contadorrevistanovo=0
                        while contadorrevistanovo==0:
                            id_revista=id_revista+1
                            nome_revista=input("Digite o titulo da nova revista: ") #titulo, identificador, editora, tipo,lista_revista, edicao, qntd
                            revista=Revista(nome_revista,id_revista,input("Digite a editora da revista: "),'R',lista_revista,input("Digite a edição da revista: "),input("Digite a quantidade de cópias da revista que você irá adicionar: "))
                            print(revista.exibir())
                            ac=input("As informações da nova revista estão corretas?S/N\n").lower()
                            if ac=="s":
                                contadorrevistanovo=1
                            else:
                                id_revista = id_revista-1
                    #elif decisao==2:
                        
                    #elif decisao==3:
                        
                    #elif decisao==4:
                        
                    else:
                        Login = False
                        adm = False
                        break
                else:
                    Login = False
                    adm = False
                    break
            elif(Decisao == 0):
                Login = False
                adm = False
                break
