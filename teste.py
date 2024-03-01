from veiculos import *
tipo=input("escolha o tipo do seu veiculo:\nC para Carro:\nM para moto:\n")
marca=input("qual a marca do seu veiculo:\n")
ano=int(input("Qual o ano do seu veiculo:\n"))
preco=float(input("Qual o preço do veiculo:\n"))
if(ano>=1 and preco>0):
    if(tipo=="C" or tipo=="c"):
        modelo=input("qual o modelo do seu carro:\n")
        potencia=int(input("qual a potencia do seu carro:\n"))
        Carro=carro(marca,ano,preco,modelo,potencia)
        print(Carro.exibir_info())
    elif(tipo=="M" or tipo=="m"):
        cilindrada=int(input("qual a cilindrada da sua moto:\n"))
        Moto=moto(marca,ano,preco,cilindrada)
        print(Moto.exibir_info())
    else:
        print("você escolheu o tipo errado de veiculo:")
else:
    print("vocẽ colocou numeros invalidos")