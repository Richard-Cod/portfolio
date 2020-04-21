from app import app

from flask import render_template, flash, redirect,request,url_for
from faker import Faker




from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError

from flask_diced import Diced, persistence_methods




from models import *
from forms import *



#                              ****************************************************************************************
@app.route('/ad/categorie_liste/')
def liste_categorie():
	categories = Categorie.query.all()
	return render_template('admin/categorie/liste.html',categories=categories)



@app.route('/ad/categorie_new/',methods=['GET', 'POST'])
def new_categorie():
	form=CategorieForm()
	form.type_id.choices = [(t.id, t.description) for t in Type.query.order_by('description')]
	if form.validate_on_submit():
		flash("La catégorie '{}' vient d'être créer ! ;)".format(
            form.description.data))
		categorie = Categorie(description=form.description.data,type=Type.query.get(form.type_id.data))
		db.session.add(categorie)
		db.session.commit()
		return redirect(url_for('liste_categorie'))
	return render_template('admin/categorie/form.html',form=form,methode='Créer')



@app.route('/ad/categorie_edit/<description>',methods=['GET', 'POST'])
def edit_categorie(description):
	c = Categorie.query.filter_by(description=description).first_or_404()
	if c :
		form=CategorieForm(formdata=request.form, obj=c)
		form.type_id.choices = [(t.id, t.description) for t in Type.query.order_by('description')]
		if request.method == 'POST' and form.validate_on_submit():
			flash("La catégorie '{}' devient {} ! ;)".format(
	            c.description,form.description.data))
			c.description = form.description.data
			db.session.commit()
			return redirect(url_for('liste_categorie'))
	return render_template('admin/categorie/form.html',form=form,methode='Modifier')




@app.route('/ad/categorie_remove/<description>',methods=['GET', 'POST'])
def remove_categorie(description):
	c = Categorie.query.filter_by(description=description).first_or_404()
	if c :
		db.session.delete(c)
		db.session.commit()
		flash("La suppression à bien été executé!")
	return redirect(url_for('liste_categorie'))