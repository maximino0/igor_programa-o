from hashlib import sha256
class senhas:
    def __init__(self,senha):
        cripto_senha = sha256(senha.encode()).hexdigest()
        senha_entrada= 0
        senha_saida = str(senha_entrada)
        while sha256(senha_saida.encode()).hexdigest()!= cripto_senha:
            senha_entrada= senha_entrada + 1
            senha_saida=str(senha_entrada)
        self.senha=senha_entrada 
    def exibir_informacoes(self):
        return f"a senha correta é {self.senha}"
senha = (input("digite a senha para ser criptografada: \n"))
p=senhas(senha)
print(p.exibir_informacoes())

