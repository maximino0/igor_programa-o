usuarios=[]
class User:
    def __init__(self,user,senha,tipo,Id = len(usuarios)+1):
        self.user=user
        self.senha=senha
        self.tipo=tipo
        self.Id=Id
usuarios.append(User('Guilherme','1234','user',1))
usuarios.append(User('Vinicius','5678','admin',2))
verificacao=""


