from expo import *
nome=input("digite o seu nome:\n")
tipo=input("digite P para professor e A para administrativo:\n")
salario=input("digite o seu salario:\n")
matricula=input("digite a sua matricula:\n")
if(tipo=="p" or tipo=="P"):
    disciplina=input("digite a sua disciplina de aula:\n")
    professor=Professor(nome,salario,matricula,disciplina)
    print(professor.exibir_info())
elif(tipo=="A" or tipo=="a"):
    cargo=input("digite o seu cargo:\n")
    admin=Administrativo(nome,salario,matricula,cargo)
    print(admin.exibir_info())
else:
    print("você escolheu o tipo errado")