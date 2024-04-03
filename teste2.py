elif func:
        while True:
            LimparTerminal()        
            Decisao = EntradaInteiraMaiorIgualQueZero("Escolha o que deseja fazer:\n1 - Opções sobre Livros, Jornais e Revistas\n2 - Editar Informações dos Clientes\n0 - SAIR\n")
            LimparTerminal()
            if (Decisao != 0):
                Decisao=Decisao+1 
            if(Decisao==2):
                tipo=EntradaInteiraMaiorIgualQueZero("Escolha qual tipo você quer: \n1-Livros\n2-Jornal\n3-Revistas\n0-Sair\n")
                if tipo==1:
                    LimparTerminal()           
                    decisao=EntradaInteiraMaiorIgualQueZero("Você escolheu a opção sobre Livros:\nO que deseja fazer 1-Adicionar Livros 2-empréstimo de Livros 0-Sair \n ")
                    LimparTerminal()
                    if (len(lista_livro)==1 and decisao!=1):
                        decisao_imp=input("Não tem nenhum Livro ainda, deseja adicionar agora: S/N \n Se a resposta for não você irá deslogar por conta de erro humano: ").lower()
                        if decisao_imp== "s":    
                            decisao=1
                        else:
                            print("Ok, voltando o sistema.\nErrar é humano.")
                            Login = False
                            adm = False
                            break
                    if decisao==1:
                        senha_correta=0
                        while senha_correta<3:
                            if Criptografar(input("Digite a senha do ADM para ter permissão de acesso"))==SENHAS[0]:
                                contadorlivronovo=0
                                while contadorlivronovo==0:
                                    id_livro=id_livro+1
                                    livro=Livro(input("Digite o titulo do novo livro: "),id_livro,input("Digite a editora do livro:"),'L',input("Digite a quantidade de cópias desse livro que você irá adicionar: "),lista_livro,input("Digite o ano de publicação do livro: "),input("Digite a edição do livro: "),input("Digite o autor do livro: "))
                                    LimparTerminal()
                                    print(livro.exibir())
                                    #(input("As informações do novo livro estão corretas?S/N\n")).lower()
                                    print("esse numero "+str(lista_livro[id_livro][1])+" é o ID do livro, guarde ele para identificação.")
                                    if input("As informações do novo livro estão corretas?S/N\n").lower()=="s":
                                        LimparTerminal()
                                        contadorlivronovo=1
                                    else:
                                        LimparTerminal()
                                        print("Então iremos recomeçar o processo de cadastro:")
                                        id_livro = id_livro-1
                            else:
                                if senha_correta==3:
                                    print("Acabaram as chances reiniciaremos o programa.")
                                    func = False
                                    Login = False
                                    break
                                else:
                                print("Senha incorreta, você tem mais "+str(3-senha_correta)+" chances.")
                                senha_correta=senha_correta+1
                                
                    elif decisao==2:
                        LimparTerminal()
                        x=int(input("você escolheu a opção de excluir um livro.\nColoque o id do livro que você quer excluir: "))
                        if x>id_livro:
                            LimparTerminal()
                            print("você escolheu um ID errado logo retornaremos ao inicio.")
                            Login = False
                            adm = False
                            break
                        else:
                            quantidade_excluir=int(input("você escolheu o livro "+str(lista_livro[x][0])+" ele tem "+str(lista_livro[x][3])+" cópias.\nVocê quer excluir quantas cópias? "))
                            if quantidade_excluir>int(lista_livro[x][3]) or quantidade_excluir<=0:
                                LimparTerminal()
                                print("você escolheu uma quantidade errada, logo assumiremos como um erro e voltaremos ao inicio do programa. ")
                                Login = False
                                adm = False
                                break
                            else:
                                lista_livro[x][3]=int(lista_livro[x][3])-quantidade_excluir
                                LimparTerminal()
                                print("agora você tem "+str(lista_livro[x][3])+" cópias do livro "+str(lista_livro[x][0])+".") 
                                if int(lista_livro[x][3])==0:
                                    LimparTerminal()
                                    print("Agora não tem nenhuma cópia do livro "+str(lista_livro[x][0])+" , logo iremos excluir ele do sistema.")
                                    lista_livro[x]="nulo"                   
                    #elif decisao==3:
                        
                    #elif decisao==4:
                        
                    else:
                        Login = False
                        adm = False
                        break
                elif tipo==2:
                    LimparTerminal()
                    decisao=EntradaInteiraMaiorIgualQueZero("Você escolheu a opção sobre Jornais:\nO que deseja fazer 1-Adicionar Jornais 2-Excluir Jornais 3-Mudar informações dos Jornais 4-empréstimo de jornais 0-Sair ")
                    if (len(lista_jornal)==1 and decisao!=1):
                        decisao_imp=input("Não tem nenhum jornal ainda, deseja adiocionar agora: S/N\nSe a resposta for não você irá deslogar por conta de erro humano:\n").lower()
                        if decisao_imp== "s":    
                            decisao=1
                            LimparTerminal()
                        else:
                            LimparTerminal()
                            print("Ok, voltando o sistema.\nErrar é humano.")
                            Login = False
                            adm = False
                            break
                    if decisao==1:
                        contadorjornalnovo=0
                        while contadorjornalnovo==0:
                            id_jornal=id_jornal+1
                            nome_jornal=input("Digite o titulo do novo jornal: ") 
                            jornal=Jornal(nome_jornal,id_jornal,input("Digite a editora do jornal: "),'J',lista_jornal,input("Digite a data de publicação do jornal: "),input("Digite a quantidade de cópias do jornal que você irá adicionar: "))
                            LimparTerminal()
                            print("esse numero "+str(lista_jornal[id_jornal][1])+" é o ID do jornal, guarde ele para identificação.")
                            print(jornal.exibir())
                            ac=input("As informações do novo jornal estão corretas?S/N\n").lower()
                            if ac=="s":
                                LimparTerminal()
                                contadorjornalnovo=1
                            else:
                                LimparTerminal()
                                print("Então iremos recomeçar o processo de cadastro:")
                                id_jornal = id_jornal-1
                    elif decisao==2:
                        LimparTerminal()
                        x=int(input("você escolheu a opção de excluir uma quantidade de jornal.\nColoque o id do jornal que você quer excluir: "))
                        if x>id_jornal:
                            LimparTerminal()
                            print("você escolheu um ID errado logo retornaremos ao inicio.")
                            Login = False
                            adm = False
                            break
                        else:
                            quantidade_excluir=int(input("você escolheu o jornal "+str(lista_jornal[x][0])+" ele tem "+str(lista_jornal[x][3])+" cópias.\nVocê quer excluir quantas cópias? "))
                            if quantidade_excluir>int(lista_jornal[x][3]) or quantidade_excluir<=0:
                                LimparTerminal()
                                print("você escolheu uma quantidade errada, logo assumiremos como um erro e voltaremos ao inicio do programa. ")
                                Login = False
                                adm = False
                                break
                            else:
                                lista_jornal[x][2]=int(lista_jornal[x][3])-quantidade_excluir
                                LimparTerminal()
                                print("agora você tem "+str(lista_jornal[x][3])+" cópias do jornal "+str(lista_jornal[x][0])+".") 
                                if int(lista_jornal[x][3])==0:
                                    LimparTerminal()
                                    print("Agora não tem nenhuma cópia do jornal "+str(lista_jornal[x][0])+" , logo iremos excluir ele do sistema.")
                                    lista_jornal[x]="nulo"   
                    #elif decisao==3:
                        
                    #elif decisao==4:
                        
                    else:
                        Login = False
                        adm = False
                        break
                elif tipo==3:
                    decisao=EntradaInteiraMaiorIgualQueZero("Você escolheu a opção sobre Revistas:\nO que deseja fazer 1-Adicionar Revistas 2-Excluir Revistas 3-Mudar informações das revistas 4-empréstimo de revistas 0-Sair ")
                    if (len(lista_revista)==1 and decisao!=1):
                        LimparTerminal()
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
                            LimparTerminal()
                            print("esse numero "+str(lista_revista[id_revista][1])+" é o ID da revista, guarde ele para identificação.")
                            print(revista.exibir())
                            ac=input("As informações da nova revista estão corretas?S/N\n").lower()
                            if ac=="s":
                                LimparTerminal()
                                contadorrevistanovo=1
                            else:
                                LimparTerminal()
                                print("Então iremos recomeçar o processo de cadastro:")
                                id_revista = id_revista-1
                    elif decisao==2:
                        LimparTerminal()
                        x=int(input("você escolheu a opção de excluir uma quantidade de revista.\nColoque o id da revista que você quer excluir: "))
                        if x>id_revista:
                            LimparTerminal()
                            print("você escolheu um ID errado logo retornaremos ao inicio.")
                            Login = False
                            adm = False
                            break
                        else:
                            quantidade_excluir=int(input("você escolheu a revista "+str(lista_revista[x][0])+" ela tem "+str(lista_revista[x][3])+" cópias.\nVocê quer excluir quantas cópias? "))
                            if quantidade_excluir>int(lista_revista[x][3]) or quantidade_excluir<=0:
                                LimparTerminal()
                                print("você escolheu uma quantidade errada, logo assumiremos como um erro e voltaremos ao inicio do programa. ")
                                Login = False
                                adm = False
                                break
                            else:
                                lista_revista[x][3]=int(lista_revista[x][3])-quantidade_excluir
                                LimparTerminal()
                                print("agora você tem "+str(lista_revista[x][3])+" cópias da revista "+str(lista_revista[x][0])+".") 
                                if int(lista_revista[x][3])==0:
                                    LimparTerminal()
                                    print("Agora não tem nenhuma cópia da revista "+str(lista_revista[x][0])+" , logo iremos excluir ele do sistema.")
                                    lista_revista[x]="nulo"
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
