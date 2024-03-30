from Classes import *
lista_livro = []
lista_revista = []
lista_jornal = []
caracter = []
titulo= 'senhor'
id = 1
publicacao ='2003'
tipo = 'L'
mes = 'novembro'
edicao = 'premium'
volume = '4'

resultado = Livro(titulo,id,publicacao,tipo,caracter,lista_livro,mes,edicao,volume)
#,caracter,lista_livro,'novembro','terceira','quarto' )
print(resultado.exibir())
