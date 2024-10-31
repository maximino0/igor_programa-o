from flask import Flask, render_template
from datetime import timedelta
from controllers.controller import*

app=Flask(__name__)

app.register_blueprint(login_controller)
app.secret_key = "sua-chave-secreta"
app.config['SESSION_COOKIE_SECURE'] = True
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)
if '__main__'==__name__:
    app.run(debug=True)