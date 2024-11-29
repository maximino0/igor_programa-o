from database import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nome= db.Column(db.String(80),nullable = True)
    email = db.Column(db.String(120), nullable = False)

    posts = db.relationship("Post", back_populates = "autor", lazy = True)

    def to_Json(self):
        return {"id": self.id , "nome" : self.nome , "email": self.email , "posts": [post.to_Json() for post in self.posts]}