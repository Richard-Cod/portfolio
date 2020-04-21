from app import db


from datetime import datetime

import enum
from werkzeug.security import generate_password_hash ,check_password_hash


class operationTypeEnum(enum.Enum):
    depot = 'depot'
    retrait = 'retrait'



# persistence_methods is a class decorator that adds save and delete methods
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(64))
    email=db.Column(db.String(120))
    sujet=db.Column(db.String(120))
    message = db.Column(db.Text)
    
    def populate_from_form(self,form):
        self.nom = form.nom.data
        self.email = form.email.data
        self.sujet = form.sujet.data
        self.message = form.message.data
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
  


