class Funcionario:
    def __init__(self, nome, salario, matricula):
        self.nome = nome 
        self.salario = salario 
        self.matricula = matricula 
    def exibir_info (self):
        return f"Nome: {self.nome}, Salário: R${self.salario}, Matricula: {self.matricula}"
class Professor(Funcionario):
    def __init__(self,nome,salario,matricula,disciplina):
        super().__init__(nome,salario,matricula)
        self.disciplina = disciplina
    def exibir_info (self):
        return super().exibir_info() + f", Disciplina: {self.disciplina}"
class Administrativo(Funcionario):
    def __init__(self,nome,salario,matricula,cargo):
        super().__init__(nome,salario,matricula)
        self.cargo = cargo
    def exibir_info (self):
        return super().exibir_info() + f", Disciplina: {self.cargo}"