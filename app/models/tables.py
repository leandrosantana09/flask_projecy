from app import db


class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    
    def __init__(self, id, username, password, name, email): # campos obrigatorios para definição da classe 
        self.username = username
        self.password = password
        self.name = name
        self.emai = email
        
    def __repr__(self):
        return "<User %r>" % self.username
     
     
     
class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.Text)
    
    user = db.relationship('User', foreign_key=user_id)
    
    def __init__(self, id_user, content): 
        self.id_user = id_user
        self.content = content

        
    def __repr__(self):
        return "<Post %r>" % self.id
    
    
class Follow(db.Model):
    __tablename__ = "follow"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('user .id'))    
    content = db.Column(db.Text)
    
    user = db.relationship('User', foreign_key=user_id)
    follower = db.relationship('User', foreign_key=follower_id)
    
    def __init__(self, id_user, content): 
        self.id_user = id_user
        self.content = content

        
    def __repr__(self):
        return "<Follow %r>" % self.id    