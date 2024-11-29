from flask import Flask, jsonify
from database import iniciar_db,db
from model.User import User
from controller.user_controller import userController


app = Flask(__name__)
app.register_blueprint(userController)

iniciar_db(app)




if __name__=="__main__":
    app.run()
