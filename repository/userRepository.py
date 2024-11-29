from dao import UserDao
from model import User , db

class UserRepository:
    def __init__(self):
        self.userDao = UserDao()

    def Buscar_Todos_Usuarios(self):
        return User.query.all()
    
    def Buscar_Todos_Usuarios_json(self):
        users=self.userDao.Buscar_Todos_Usuarios()
        usera=[]
        for i in users:
            usera.append(i.to_Json())
        return usera

    def Adicionar_Usuarios(self,nome,email):
        user = User(nome=nome, email=email)
        db.session.add(user)
        db.session.commit()

        