from app import app

from flask import render_template, flash, redirect,request,url_for




from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError

from flask_diced import Diced, persistence_methods




from models import *
from forms import *



#----------------------------------------------------------------------------------------------------------------------------------
navs = {
    
		"Application":{
			"Contacts":"contact",
			"uilisateurs":"user"
		},
		"Fonctionnalités":{
			"Contacts":'contact_liste',
			"uilisateurs":'user_liste'
		},
		"troisieme":{
			"Contacts":'contact_liste',
			"uilisateurs":'user_liste'
		}
	}



@app.route('/ad/contact/')
def contact_liste():
    contacts = Contact.query.all()
    return render_template('admin/contact/liste.html',data = contacts,navs=navs,titre="Contacts")


@app.route('/ad/categorie_remove/<id>',methods=['GET', 'POST'])
def contact_remove(id):
	c = Contact.query.filter_by(id=id).first_or_404()
 
	if c :
		db.session.delete(c)
		db.session.commit()
		flash("La suppression à bien été executé!","success")
	return redirect(url_for('contact_liste'))



@app.route('/ad/user/')
def user_liste():
    users = User.query.all()
    return render_template('admin/contact/liste.html',data = users,navs=navs,titre="Utilisateurs")


@app.route('/ad/user/<id>',methods=['GET', 'POST'])
def user_remove(id):
	c = User.query.filter_by(id=id).first_or_404()
	if c :
		db.session.delete(c)
		db.session.commit()
		flash("La suppression à bien été executé!","success")
	return redirect(url_for('user_liste'))


