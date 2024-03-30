#Classes de Pessoas

class Humano:
    def __init__(self,nome,cpf,email,telefone,endereco):
      self._nome=nome
      self._cpf=cpf
      self._email=email
      self._telefone=telefone
      self._endereco=endereco

class Cliente(Humano):
    def __init__(self,nome,cpf,email,telefone,endereco,id_cliente,emprestimo):
        super().__init__(nome,cpf,email,telefone,endereco)
        self.id_cliente=id_cliente       #ID_CLIENTE
        self.emprestimo=emprestimo    #Empréstimo
        cliente = []
        cliente.append(nome)
        cliente.append(cpf)
        cliente.append(email)
        cliente.append(telefone)
        cliente.append(endereco)
        cliente.append(id_cliente)
        cliente.append(emprestimo)
        lista_cliente = []
        lista_cliente.append(cliente)
     

class Funcionario(Humano):
    def __init__(self,nome,cpf,email,telefone,endereco,id_funcionario,login,senha,salario,horas):
        super().__init__(nome,cpf,email,telefone,endereco)
        self.__id_funcionario=id_funcionario    #ID_FUNCIONARIO
        self.login=login    #login
        self.senha=senha    #senha
        self.__salario=salario    #salário
        self.__horas=horas    #horas trabalhadas
        funcionario = []
        funcionario.append(nome)
        funcionario.append(cpf)
        funcionario.append(email)
        funcionario.append(telefone)
        funcionario.append(endereco)
        funcionario.append(id_funcionario)
        funcionario.append(login)
        funcionario.append(senha)
        funcionario.append(salario)
        funcionario.append(horas)
        lista_funcionario = []
        lista_funcionario.append(funcionario)


class Admin:
    def __init__(self,login_m,senha_m,pergunta):
        self.__login_m=login_m  #login master
        self.__senha_m=senha_m  #senha master
        self.__pergunta_m=pergunta
            
          
     

#Classes de Livros

class Papel:
    def __init__(self,titulo,id,publicacao,tipo,caracter):
        caracter = []
        self.titulo=titulo    #Título
        self.id=id    #ID
        self.publicacao=publicacao    #Publicação (ano)
        self.tipo=tipo
    def exibir(self,caracter):
        pass
     

class Livro(Papel):
    def __init__(self,titulo,id,publicacao,tipo,caracter,lista_livro,mes,edicao,volume):
        super().__init__(titulo,id,publicacao,tipo,caracter)
        self.mes=mes    #Mês
        self.edicao=edicao    #Edição
        self.volume=volume    #Volume
        caracter.append(titulo)
        caracter.append(id)
        caracter.append(publicacao)
        caracter.append(mes)
        caracter.append(edicao)
        caracter.append(volume)
        lista_livro.append(caracter)
        self.lista=lista_livro
    def exibir(self):
        return f"{self.lista}"
     

class Revista(Papel):
    def __init__(self,titulo,id,publicacao,tipo,caracter,lista_revista,semana):
        super().__init__(titulo,id,publicacao,tipo,caracter,lista_revista)
        self.semana=semana
        caracter.append(titulo)
        caracter.append(id)
        caracter.append(publicacao)
        caracter.append(semana)
        lista_revista.append(caracter)
        self.lisa=lista_revista
    def exibir(self):
        return f"{self.lisa}"
            #semana
     

class Jornal(Papel):
    def __init__(self,titulo,id,publicacao,tipo,caracter,lista_jornal,dia):
        super().__init__(titulo,id,publicacao,tipo,caracter,lista_jornal)
        self.dia=dia
        caracter.append(titulo)
        caracter.append(id)
        caracter.append(publicacao)
        caracter.append(dia)
        lista_jornal.append(caracter)
        self.list=lista_jornal
    def exibir(self):
        return f"{self.list}"
    #dia
