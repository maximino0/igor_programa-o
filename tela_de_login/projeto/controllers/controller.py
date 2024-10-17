from flask import Flask, Blueprint, render_template,request,redirect,url_for
from models.model import*

login_controller=Blueprint('login',__name__)
@login_controller.route('/')
def index():
    return render_template('index.html',usuarios=usuarios,verificacao=verificacao)
@login_controller.route("/user", methods=['POST'])
def ver():
    nome=request.form['nome']
    senha=request.form['Senha']
    for i in usuarios:
        if (i['Nome']==nome and i['Senha']==senha):
            verificacao=f'<p>Você foi conectado com sucesso {i["Nome"]}</p>'
            return render_template('tipo1.html',verificacao=verificacao)
    verificacao=f'<p>Esse usuário não existe</p>'
    return render_template('index.html',usuarios=usuarios,verificacao=verificacao)
    
