from database import db

class Post(db.model):
    id = db.Column(db.Integer,primary_key = True)
    titulo= db.Column(db.String(200),nullable = True)
    conteudo= db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = True)

    autor = db.relationship("User", back_populates = "posts", lazy = True)

    def to_Json(self):
        return {"id": self.id , "titulo" : self.titulo , "conteudo": self.conteudo}