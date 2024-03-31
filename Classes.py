#Classes de Pessoas

class Humano:
    def __init__(self,nome,cpf,email,telefone,endereco):
      self._nome=nome
      self._cpf=cpf
      self._email=email
      self._telefone=telefone
      self._endereco=endereco
    def exibir_info_pessoa(self):
        pass

class Cliente(Humano):
    def __init__(self,nome,cpf,email,telefone,endereco,lista_cliente,id_cliente,emprestimo):
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
        lista_cliente.append(cliente)
        self.lista_cliente=lista_cliente
    def exibir_info_pessoa(self):
        return f"{self.lista_cliente}"
     

class Funcionario(Humano):
    def __init__(self,nome,cpf,email,telefone,endereco,lista_funcionario,id_funcionario,login,senha,salario,horas):
        super().__init__(nome,cpf,email,telefone,endereco)
        self.__id_funcionario=id_funcionario    #ID_FUNCIONARIO
        self.login=login    #login
        self.senha=senha    #senha
        self.__salario=salario    #salário
        self.__horas=horas      #horas trabalhadas
        self._nome=nome    
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
        self.funcionario=funcionario
        lista_funcionario.append(funcionario)
    def exibir_info_pessoa(self):
        return f"{self.funcionario}"


class Admin:
    def __init__(self,login_m,senha_m,pergunta):
        self.__login_m=login_m  #login master
        self.__senha_m=senha_m  #senha master
        self.__pergunta_m=pergunta
    def exibi(self):
        return f"o login é:{self.__login_m}\na senha é:{self.__senha_m}\na pergunta é:{self.__pergunta_m}\n"
            

#Classes de Livros

class Papel:
  def _init_(self, titulo, identificador, editora, tipo, qntd):
      self.titulo = titulo  # Título
      self.identificador = identificador  # Identificador
      self.editora = editora  # Publicação (ano)
      self.tipo = tipo
      self.qntd = qntd

  def exibir(self):
      pass


class Livro(Papel):
  def _init_(self, titulo, identificador, editora, tipo, lista_livro, ano, edicao, autor, qntd):
      super()._init_(titulo, identificador, editora, tipo, qntd)
      self.ano = ano  # Ano
      self.edicao = edicao  # Edição
      self.autor = autor  # Autor
      caracteristicas = [titulo, identificador, editora, qntd, ano, edicao, autor]
      lista_livro.append(caracteristicas)
      self.lista = lista_livro
  def Exibir(self):
      return f"{self.lista}"


class Revista(Papel):
  def _init_(self, titulo, identificador, editora, tipo,lista_revista, edicao, qntd):
      super()._init_(titulo, identificador, editora, tipo, qntd)
      self.edicao = edicao 
      caracteristicas=[titulo,identificador,editora,qntd,edicao]
      lista_revista.append(caracteristicas)
      self.lista = lista_revista

  def exibir(self):
      return f"{self.lista}"


class Jornal(Papel):
  def _init_(self, titulo, identificador, editora, tipo,lista_jornal, data, qntd):
      super()._init_(titulo, identificador, editora, tipo, qntd)
      self.data = data
      caracteristicas=[titulo,identificador,editora,qntd,data]
      lista_jornal.append(caracteristicas)
      self.lista = lista_jornal

  def exibir(self):
      return f"{self.lista}"

#dia
