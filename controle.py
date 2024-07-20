alunos=[]
mat=[]
port=[]
lbp=[]
class Pessoa:
    def __init__(self, nome, email, data_de_nascimento, cpf):
        self.__nome = nome
        self.__email = email
        self.__data = data_de_nascimento
        self.__cpf = cpf
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_data(self):
        return self.__data
    def get_cpf(self):
        return self.__cpf
class Aluno(Pessoa):
    def __init__(self,nome, email, data_de_nascimento, cpf,matricula):
        super().__init__( nome, email, data_de_nascimento, cpf)
        self.__matricula=matricula
    def get_matricula(self):
        return self.__matricula
class Materia(Aluno):
    def __init__(self,materia, nome_p, carga_horaria, falta,nome, email, data_de_nascimento, cpf,matricula):
        super().__init__(nome, email, data_de_nascimento, cpf,matricula)
        self.__materia=materia
        self.__nome_p =nome_p
        self.__carga = carga_horaria
        self.__falta = falta
    def get_materia(self):
        return self.__materia
    def get_nome_p(self):
        return self.__nome_p
    def get_carga(self):
        return f"{self.__carga} horas"
    def get_falta(self):
        return self.__falta
class Professor(Materia):
    def __init__(self,nome, email, data_de_nascimento, cpf,salario,materia,carga_horaria):
        super().__init__(nome, email, data_de_nascimento, cpf,materia,carga_horaria)
        self.__salario=salario
    def get_salario(self):
        return self.__salario
class Nota(Materia):
    def __init__(self, nota_1, nota_2,materia,nome_p, carga_horaria, falta,nome,email,data_de_nascimento,cpf,matricula):
        super().__init__(materia, nome_p, carga_horaria, falta,nome, email, data_de_nascimento, cpf,matricula)
        self.__nota_1 = nota_1
        self.__nota_2 = nota_2
        self.__media = (self.__nota_1 + self.__nota_2) / 2
        if nota_1 < nota_2:
            self.__menor_nota = nota_1
            self.__maior_nota = nota_2
        else:
            self.__menor_nota = nota_2
            self.__maior_nota = nota_1
    def get_nota_1(self):
        return self.__nota_1
    def get_nota_2(self):
        return self.__nota_2
    def get_menor_nota(self):
        return self.__menor_nota
    def get_maior_nota(self):
        return self.__maior_nota
    def get_media(self):
        return self.__media
    def imprimir_dados(self):
        resultado={"O nome do aluno":self.get_nome(),
                "A materia":self.get_materia(),
                "A carga horária": self.get_carga(),
                "As faltas":self.get_falta(),
                "O nome do professor":self.get_nome_p(),
                "O email do aluno": self.get_email(),
                "A data de nascimento":self.get_data(),
                "O cpf do aluno":self.get_cpf(),
                "A matricula":self.get_matricula(),
                "A primeira nota do aluno":self.get_nota_1(),
                "A segunda nota do aluno":self.get_nota_2(),
                "media do aluno":self.get_media()}
        if resultado.get("A materia").upper()=="MATEMATICA":
            mat.append(', '.join(f"{chave}: {valor}" for chave, valor in resultado.items()))
        elif resultado.get("A materia").upper()=="PORTUGUES":
            port.append(', '.join(f"{chave}: {valor}" for chave, valor in resultado.items()))
        elif resultado.get("A materia").upper()=="PROGRAMACAO":
            lbp.append(', '.join(f"{chave}: {valor}" for chave, valor in resultado.items()))
        saida = ', '.join(f"{chave}: {valor}\n" for chave, valor in resultado.items())
        print(f"{saida}") 
        print(f"histórico de matemática: {mat}\n")
        print(f"Histórico de portugues: {port}\n")
        print(f"historico de programação{lbp}\n")
for i in range(2):
    nome = input("Digite o nome do aluno: ")
    materia = input("Digite a matéria: ")
    carga_horaria = int(input("Digite a carga horária: "))
    faltas = int(input("Digite o número de faltas: "))
    nome_professor = input("Digite o nome do professor: ")
    email_aluno = input("Digite o email do aluno: ")
    data_nascimento = input("Digite a data de nascimento (DD-MM-YYYY): ")
    cpf_aluno = input("Digite o CPF do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    exemplo = Nota(nota1, nota2, materia, nome_professor, carga_horaria, faltas, nome, email_aluno, data_nascimento, cpf_aluno, matricula)
    exemplo.imprimir_dados()
