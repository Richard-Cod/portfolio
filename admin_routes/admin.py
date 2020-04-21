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



#----------------------------------------------------------------------------------------------------------------------------------


@app.route('/ad/base/')
def base():
	return render_template('admin/adbase.html')




@app.route('/ad/chart/')
def chart():
	#plats = Plat.query.all()
	return render_template('admin/charts.html')
