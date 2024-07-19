class Pessoa:
    def __init__(self, nome, email, data_de_nascimento, cpf):
        self.nome = nome
        self.email = email
        self.data = data_de_nascimento
        self.cpf = cpf
class Aluno(Pessoa):
    def __init__(self,nome, email, data_de_nascimento, cpf,matricula):
        super().__init__( nome, email, data_de_nascimento, cpf)
        self.matricula=matricula
class Materia(Aluno):
    def __init__(self,materia, nome_p, carga_horaria, falta,nome, email, data_de_nascimento, cpf,matricula):
        super().__init__(nome, email, data_de_nascimento, cpf,matricula)
        self.materia=materia
        self.nome_p = nome_p
        self.carga = carga_horaria
        self.falta = falta
class Professor(Pessoa):
    def __init__(self,nome, email, data_de_nascimento, cpf,salario):
        super().__init__(self, nome, email, data_de_nascimento, cpf)
class Nota(Materia):
    def __init__(self, nota_1, nota_2,materia,nome_p, carga_horaria, falta,nome,email,data_de_nascimento,cpf,matricula):
        super().__init__(materia, nome_p, carga_horaria, falta,nome, email, data_de_nascimento, cpf,matricula)
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.media = (self.nota_1 + self.nota_2) / 2
        if nota_1 < nota_2:
            self.menor_nota = nota_1
            self.maior_nota = nota_2
        else:
            self.menor_nota = nota_2
            self.maior_nota = nota_1
    def imprimir_dados(self):
        resultado={"nome":self.nome,
                   "materia":self.materia,
                   "carga horária": self.carga,
                   "faltas":self.falta,
                   "nome do professor":self.nome_p,
                   "email do aluno": self.email,
                   "data de nascimento":self.data,
                   "cpf do aluno":self.cpf,
                   "matricula":self.matricula,
                   "primeira nota do aluno":self.nota_1,
                   "segunda nota do aluno":self.nota_2,
                   "media do aluno":self.media}
        print(resultado)      
nota_exemplo = Nota(8, 7, "Matemática", "João", 60, 5,"enzo" ,"joao@email.com", "2000-01-01", "123.456.789-00", "A123")
nota_exemplo.imprimir_dados()
