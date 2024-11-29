from flask import Blueprint, jsonify
from dao import UserDao
from repository.userRepository import UserRepository

qualquer= UserRepository()
userController= Blueprint("user", __name__)

@userController.route("/")
def index():
    return "Olá"

@userController.route("/add")
def adic():
    UserDao.Adicionar_Usuarios("Pedro","Pedrinho@pedro.com")
    return "Adicionado com success"

@userController.route("/ver")
def veri():
    return qualquer.Buscar_Todos_Usuarios_json()