from app import app
from data import *

from flask import render_template, flash, redirect,request,url_for




from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError

from flask_diced import Diced, persistence_methods




from models import *
from forms import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('client/index.html',info=info,myself=myself,parcours=parcours,exp=exp,technos=technos,projets=projets,temoignages=temoignages)
  

  
@app.route('/blog')
def blog():
	return render_template('client/blog.html')

@app.route('/blog/<id>')
def blog_show(id):
	return render_template('client/single-blog.html')
  

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            obj = Contact()
            obj.populate_from_form(form)
            obj.save_to_db()

            flash(f"Merci pour votre message {obj.nom} ;) ",'success')
            return redirect(url_for('contact'))

        elif request.method == 'POST':
            flash(f"Remplissez tous les champs svp 👍",'danger')
            print(form.errors)
    return render_template('client/contact.html',form=form,info=info)



