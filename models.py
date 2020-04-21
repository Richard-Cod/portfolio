from app import db


from datetime import datetime

import enum

class operationTypeEnum(enum.Enum):
    depot = 'depot'
    retrait = 'retrait'



# persistence_methods is a class decorator that adds save and delete methods
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    commandes = db.relationship('Commande',backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)  

  
#types = ['petit déjeuné','déjeuné','diné','fast food']
class Type(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(120), nullable=False)
	categories = db.relationship('Categorie',backref='type', lazy=True)





#categorie = ['pizza','hamburger','wraps','kebabs','riz','couscous','fritures']
class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    plats = db.relationship('Plat', backref='categorie', lazy=True,cascade="save-update, merge, delete")
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'),nullable=False)

        



#plats = ['pizza reine','cheese burger','riz sauce tomate']


class Plat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(64), index=True, unique=True,nullable=False)
    description = db.Column(db.Text(),nullable=False)
    prix = db.Column(db.Integer,nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'),nullable=False)
    detail_id = db.Column(db.Integer, db.ForeignKey('detail.id'),nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.nom)   





class Compte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description=db.Column(db.Text())
    solde = db.Column(db.Integer, nullable=False)
    operations = db.relationship('Operation', backref='compte', lazy=True,cascade="save-update, merge, delete")

    def depot(self,valeur):
        self.solde+=abs(valeur)
        operation = Operation(valeur=valeur,compte=self,type=operationTypeEnum.depot)
        db.session.add(operation)
        db.session.commit()

    def retrait(self,valeur):
        if self.solde>=abs(valeur):
            self.solde-=valeur
            operation = Operation(valeur=valeur,compte=self,type=operationTypeEnum.retrait)
            db.session.add(operation)
            db.session.commit()

    def get_revenue_by_month(self):
        l=[0,0,0,0,0,0,0,0,0,0,0,0]
        for op in self.operations:
            if op.type== operationTypeEnum.depot:
                l[op.date.month -1]+=op.valeur
            elif op.type== operationTypeEnum.retrait:
                l[op.date.month -1]-=op.valeur

        return l

    def get_revenue_by_year(self):
        d={}
        for op in self.operations:
            d[op.date.year] =0

        for op in self.operations:
            if op.type== operationTypeEnum.depot:
                print(d)
                d[op.date.year]+= op.valeur
            elif op.type== operationTypeEnum.retrait:
                print(d)
                d[op.date.year]-= op.valeur


        #merged_list = [(l[i], m[i]) for i in range(0, len(l))] 



        return d


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime,default=datetime.utcnow,index=True,nullable=False)
    valeur=db.Column(db.Integer, nullable=False)
    compte_id = db.Column(db.Integer, db.ForeignKey('compte.id'),nullable=False)
    type = db.Column(db.Enum(operationTypeEnum), nullable=False)


class Commande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime,default=datetime.utcnow,index=True,nullable=False)
    detail_id = db.Column(db.Integer, db.ForeignKey('detail.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=True)



class Detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plats = db.relationship('Plat',lazy=True,cascade="save-update, merge, delete")
    commande = db.relationship('Commande',lazy=True,cascade="save-update, merge, delete",uselist=False)
    #compte_id = db.Column(db.Integer, db.ForeignKey('compte.id'),nullable=False)


"""

from models import *
from cantine import db
c= Compte(description='Compte principale du restaurant',solde=0)

"""
#dans personnes
"""
addresses = db.relationship('Address', backref='person', lazy=True)


#Dans adreess

person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)
"""
#c = Categorie(description='petit dejeuner')



#plat = Plat(nom='Pizza reine',description='pizza,champignons,fromage,jambon (halal)',prix=4500,categorie=pizza)