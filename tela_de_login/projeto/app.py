from flask import Flask, render_template
from controllers.controller import*

app=Flask(__name__)
app.register_blueprint(login_controller)
if '__main__'==__name__:
    app.run(debug=True)