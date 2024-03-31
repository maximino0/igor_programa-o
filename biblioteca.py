from FuncoesEBibliotecas import *
from Classes import *
LimparTerminal()

SENHAS = ["Provisório"]
FUNCIONARIO = []
CaracteristicasFUNCIONARIO = []
lista_livro = []
lista_revista = []
lista_jornal = []
lista_funcionario = []
lista_cliente = []
funcionarios = []
adm = False
Login = False
id_funcionario = 0
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
                print("Acesso Liberado.") #Podemos adicionar uma variável {nome[ID]} e colocarmos algo como "Acesso Liberado Pedro"
                Login = True
                LimparTerminal()
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
                            funcionarios=Funcionario(input("Digite o nome do funcionario que você irá adicionar: \n"),EntradaCPF(input("Digite o cpf do novo funcionário:")),input("Digite o email do novo funcionário: \n"),EntradaCPF(input("Digite o telefone do novo funcionário: \n")),(input("Digite o endereço: ")),lista_funcionario,id_funcionario,id_funcionario,input("Digite a senha do login do novo funcionário: \n"),input("digite o salário: \n"),input("Quantas horas ele deverá trabalhar mensalmente: \n"))
                            print(funcionarios.exibir_info_pessoa())
                            abc=input("As informações do novo funcionário estão corretas?S/N").lower()
                            if abc=="s":
                                contadorfuncionarionovo=1
                            else:
                                id_funcionario = id_funcionario-1
                        #FUNCIONARIO.append(lista_funcionario) nn precisa mais disso pq o lista_funcionario ja faz essa função
                        print(lista_funcionario)
                        funcionarios = [] #Resetar a lista pro próximo uso
                        ID = len(SENHAS) 
                        VerificarSenhas(SENHAS, f"Insira a senha do funcionário de ID {ID} para revisão: ", ID)
                        LimparTerminal()
                    else:
                        print("Ok, voltando o sistema.\nErrar é humano.")  
                elif(len(SENHAS>=2)):
                    xyz=input("Escolha o que deseja fazer sobre os funcionários:\n1 - Adicionar funcionário\n2 - Excluir algum funcionário\n3 - Editar Informações dos funcionários\n0 - SAIR\n") 
                    if xyz=='1':
                        contadorfuncionarionovo=0
                        while contadorfuncionarionovo==0:
                            id_funcionario = id_funcionario+1
                            funcionarios=Funcionario(input("Digite o nome do funcionario que você irá adicionar: \n"),EntradaCPF(input("Digite o cpf do novo funcionário:")),input("Digite o email do novo funcionário: \n"),EntradaCPF(input("Digite o telefone do novo funcionário: \n")),(input("Digite o endereço: ")),lista_funcionario,id_funcionario,id_funcionario,input("Digite a senha do login do novo funcionário: \n"),input("digite o salário: \n"),input("Quantas horas ele deverá trabalhar mensalmente: \n"))
                            print(funcionarios.exibir_info_pessoa())
                            abc=input("As informações do novo funcionário estão corretas?S/N").lower()
                            if abc=="s":
                                contadorfuncionarionovo=1
                            else:
                                id_funcionario = id_funcionario-1
                        #FUNCIONARIO.append(lista_funcionario) nn precisa mais disso pq o lista_funcionario ja faz essa função
                        print(lista_funcionario)
                        funcionarios = [] #Resetar a lista pro próximo uso
                        ID = len(SENHAS) 
                        VerificarSenhas(SENHAS, f"Insira a senha do funcionário de ID {ID} para revisão: ", ID)
                        LimparTerminal()
                    elif xyz=='0':
                        Login = False
                        adm = False
                        break
            elif(Decisao == 0):
                Login = False
                adm = False
                break
