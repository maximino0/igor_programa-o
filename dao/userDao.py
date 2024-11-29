from model import User 
from database import db
from flask import jsonify

class UserDao:
    @staticmethod
    def Buscar_Todos_Usuarios():
        return User.query.all()
    @staticmethod
    def Adicionar_Usuarios(nome,email):
        user = User(nome=nome, email=email)
        db.session.add(user)
        db.session.commit()
    @staticmethod
    def Mostrar():
        users=UserDao.Buscar_Todos_Usuarios()
        usera=[]
        for i in users:
            usera.append(i.to_Json())
        return jsonify(usera)