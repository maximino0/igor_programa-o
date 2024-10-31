from flask import Flask, Blueprint, render_template,request,redirect,url_for,session,make_response,get_flashed_messages,flash

from models.model import*

login_controller=Blueprint('login',__name__)
rotas_publicas=["login.ver","login.index"]
@login_controller.before_request
def request_info():
    print("Executa antes da requisição.")
@login_controller.after_request
def response_info(response):
    print("Executa antes da resposta")
    return response
@login_controller.route('/')
def index():
    return render_template('index.html',usuarios=usuarios,verificacao=verificacao)
@login_controller.route("/user", methods=['POST','GET'])
def ver():
    if request.method == 'POST':
        session.permanent = True
        session['user']=request.form['user']
        for i in usuarios:
            if (i.user==session['user'] and i.senha==request.form['Senha']):
                session['Tipo']=i.tipo
                session['Id']=i.Id
                verificacao=f"<p>Você foi conectado com sucesso {session['user']}, você é um {session['Tipo']}</p>"
                flash("Login realizado com sucesso!","success")
                
                resp = make_response(render_template('tipo1.html', verificacao=verificacao))
                resp.set_cookie('user', session['user'])
                resp.set_cookie('tipo', session['Tipo'])
                resp.set_cookie('verificacao', verificacao, max_age=60*60*24)
                return resp
        verificacao=f'<p>Esse usuário não existe</p>'
        flash("Login não foi realizado com sucesso!","error")
        
        return render_template('index.html',usuarios=usuarios,verificacao=verificacao)
    else:
        session["user"]=request.cookies.get('user')
        session["tipo"]=request.cookies.get('tipo')
        if session["user"] and session["tipo"]:
            verificacao=f'<p>Você foi conectado com sucesso {session["user"]}, você é um {session["Tipo"]}</p>'
            return render_template('tipo1.html',usuarios=usuarios,verificacao=verificacao)
        else:
            flash("Você precisa estar logado para acessar essa página.")
            return redirect(url_for('login.index'))
@login_controller.route("/logout", methods=['POST'])
def logout():
    resp = make_response(redirect(url_for('login.index')))
    resp.set_cookie('user', '', expires=0)
    resp.set_cookie('tipo', '', expires=0)
    resp.set_cookie('verificacao', '', expires=0)
    flash("Você saiu com sucesso.","success")
    return resp
@login_controller.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'),404
@login_controller.errorhandler(ZeroDivisionError)
def pagina_zero_divisao(e):
    return render_template('zero.html',message="Ocorreu uma divisão por zero!"),500
@login_controller.errorhandler(Exception)
def pagina_erro_generico(e):
    return render_template('generic_error.html',message=str(e)),500