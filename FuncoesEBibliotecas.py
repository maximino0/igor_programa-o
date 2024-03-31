# Só uma ideia. Utilizar esse arquivo para colocar todas as funções e bibliotecas que iremos utilizar. Depois podemos importar somente ele.

from hashlib import sha256

from Classes import *

import time
import os
#from tabulate import tabulate #Biblioteca para printar em formato de tabela. Seria legal pra printar todos os livros, ou todos os funcionários.
# Tem que baixar digitando "pip install tabulate" no terminal, sem aspas
#Exemplo: 
#table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
#print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))

def LimparTerminal():
  time.sleep(0.4)
  os.system('cls' if os.name == 'nt' else 'clear') # Detecta se é Windows (se sim, usa o comando 'cls') ou se é baseado em Unix (Linux ou MacOS) e usa o comando 'clear'.
  
# Essa função limpa o terminal. Código de exemplo:

# print("Oi")
# LimparTerminal()

def Criptografar(texto):
  return sha256((texto).encode()).hexdigest()

def EntradaInteira(mensagem):
  while True:
    try:
      x = int(input(mensagem))
    except:
      print("Entrada inválida. Tente novamente.")
    else:
      return x
def Livro_Adicionar(caracteristicas,lista):
    while True:
        caracteristicas.append(input("Digite o título: "))
        caracteristicas.append(input("Digite o paginas: "))
        caracteristicas.append(input("Digite o autor: "))
        caracteristicas.append(input("Digite o editora: "))
        caracteristicas.append(input("Digite o data: "))
        if(input("você digitou tudo corretamente? \n S/N\n ")).upper()=='S':
            lista.append(caracteristicas)
            caracteristicas = [] #Resetar a lista
            if (input("você adicionou tudo que desejava? \n S/N\n ")).upper()=='S':
              break
        caracteristicas = [] #Resetar lista para o próximo uso

def Jornal_Adicionar(caracteristicas,lista): #mudar para atributos do jornal
    while True:
        caracteristicas.append(input("Digite o título: "))
        caracteristicas.append(input("Digite o paginas: "))
        caracteristicas.append(input("Digite o autor: "))
        caracteristicas.append(input("Digite o editora: "))
        caracteristicas.append(input("Digite o data: "))
        if(input("você digitou tudo corretamente? \n S/N\n ")).upper()=='S':
            lista.append(caracteristicas)
            caracteristicas = [] #Resetar lista para o próximo uso
            if (input("você digitou tudo que desejava? \n S/N\n ")).upper()=='S':
              break
        caracteristicas = [] #Resetar lista para o próximo uso
      
def Revista_Adicionar(caracteristicas,lista): #mudar para atributos da revista
    while True:
        caracteristicas.append(input("Digite o título: "))
        caracteristicas.append(input("Digite o paginas: "))
        caracteristicas.append(input("Digite o autor: "))
        caracteristicas.append(input("Digite o editora: "))
        caracteristicas.append(input("Digite o data: "))
        if(input("você digitou tudo corretamente? \n S/N\n ")).upper()=='S':
            lista.append(caracteristicas)
            caracteristicas = [] #Resetar lista para o próximo uso
            if (input("você digitou tudo que desejava? \n S/N\n ")).upper()=='S':
              break
        caracteristicas = [] #Resetar lista para o próximo uso

def EntradaInteiraMaiorQueZero(mensagem):
  while True:
    try:
      x = int(input(mensagem))
      if (x<=0):
        raise 
    except:
      print("Entrada inválida. Tente novamente.")
      LimparTerminal()
    else:
      return x
def EntradaInteiraMaiorIgualQueZero(mensagem):
  while True:
    try:
      x = int(input(mensagem))
      if (x<0):
        raise 
    except:
      print("Entrada inválida. Tente novamente.")
      LimparTerminal()
    else:
      return x

def EntradaCPF(mensagem): #Funciona tbm para telefone
  while True:
    try:
      x = int(input(mensagem))
      if not (len (str(x)) ==11 ):
        raise 
    except:
      print("Entrada inválida. Tente novamente.")
      LimparTerminal()
    else:
      return x

    
def CaracteristicasHumano(nome,cpf,email,telefone,endereco):
  nome=input("Digite o nome: ")
  cpf=(EntradaCPF("Digite o CPF: "))
  email=(input("Digite o e-mail: "))
  telefone=(EntradaCPF("Digite o Telefone: ")) #Entrada CPF funciona também para o telefone, desde que o código do país seja +55 kkkkkk
  endereco=(input("Digite o endereço: "))

def VerificarSenhas(ListaSenhas, Mensagem, ID):
  while True:
    ListaSenhas.append(Criptografar(input(Mensagem)))
    LimparTerminal()
    print(ListaSenhas)
    if (Criptografar(input("Repita a senha: ")) == ListaSenhas[ID]):
        print("Senha validada com sucesso!")
        break
    else:
        print("Senhas não conferem.")
        ListaSenhas.pop()
    LimparTerminal()
