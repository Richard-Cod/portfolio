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

@app.route('/')
@app.route('/index')
def index():
    info = {
		"nom":"Richard Bathiebo",
		"profession":"Développeur Web/Mobile",
		"description":"Bienvenue sur mon portfolio parcourez le et n'oubliez pas que la page de contact est là si vous voulez me joindre",
		"telephone":"+221 78 153 79 66",
		"email":"richard.bathiebo.7@gmail.com",
		"lieu":"Dakar , Sénégal"
	}
    myself = {
        "aboutMe":"Je suis en 3e année d'informatique appliquée à la gestion des entreprises passionné de Python et JavaScript",
		"nbProjets":20,
		"skills" : {
			"Html/Css":80,
			"Bootstrap":80,
			"Angular": 10,
			"React":20,
   			"Vue":10,
			
			"PHP":60,
			"Django":80,
			"Flask":80,
			"Node Js":50,
   
			"Flutter":50,
			"React-Native":20,


		}
	}
    parcours=[
		{
			"periode":"Septembre 2018-2020",
			"lieu":"Institut Nationale Universitaire Champoleon d'Albi",
			"poste":"Licence en Informatique (Double Diplomation)"
		},
		{
			"periode":"Septembre 2017-2020",
			"lieu":"Institut Supérieur de Management ,Dakar",
			"poste":"Licence en Informatique appliquée option mathématique appliquée et économétrie"
		}
	]
    exp = [
        {
			"periode":"Juillet 2018 - maintenant",
			"lieu":"Freelance",
			"poste":"Développeur Web"
		}
		
	]
    technos = [
		"Django",
		"Symfony",
		"React",
		"Wordpress"
	]
    projets = [
		{
			"techno":technos[0],
  			"image":"https://i.ytimg.com/vi/WG3pGmoo8nE/maxresdefault.jpg",
			"titre":"PmeConnect",
			"description":"Projet annuaire pme au Sénégal"
      
		},
  		{
			"techno":technos[1],
  			"image":"https://farm8.staticflickr.com/7710/17022394108_23310683ce_o.png",
			"titre":"Wari-Ism",
			"description":"Application de gestion de compte pour une start-up "
		},
   		 {
			"techno":technos[3],
  			"image":"https://s.w.org/images/home/screen-themes.png?3",
			"titre":"Tendances Sunugal",
			"description":"Site ecommerce pour un particulier"
		}
	]
    temoignages=[
		 {
			"nom":"Momar Diagne",
			"description":"Je remercierai jamais assez Richard pour ce superbe site ecommerce qui m'a permis de tripler mes revenues et d'augmenter mon audience 😃"
		},
		 {
			"nom":"Moussa Bamba",
			"description":"J'ai rarement vu quelqu'un d'aussi motivé dans la réalisation des projets"
		}
	]
    
    return render_template('client/index.html',info=info,myself=myself,parcours=parcours,exp=exp,technos=technos,projets=projets,temoignages=temoignages)
  

@app.route('/blog')
def blog():
	return render_template('client/blog.html')
  

@app.route('/contact',methods=['GET', 'POST'])
def contact():
	if request.method == 'POST':
		nom = request.form.get('name')
		email =request.form.get('email')
		sujet = request.form.get('sujet')
		message = request.form.get('message')
		flash("Utilisateur {}  Votre message a bien été envoyé".format(nom))
	return render_template('client/contact.html')
  
@app.route('/menu')
def menu():
	plats = Plat.query.all()
	return render_template('client/menu.html',plats=plats)


@app.route('/panier')
def panier():
	platsCommande = Plat.query.all()
	return render_template('client/panier.html',platsCommande=platsCommande)



  
@app.route('/about')
def about():
	return render_template('client/about_us.html')
  




@app.route('/login')
def login():
	return render_template('auth/login.html')
  


@app.route('/signin')
def signin():
	return render_template('auth/signin.html')
  






#                             ****************************************************************************

"""
	plats = [
				{
					'nom':'Pizza Margherita',
					'prix':5000,
					'image':'https://colorlib.com/preview/theme/luigis/images/seller-2-200x200.png'
				},
				{
					'nom':'Pain Poulet sans oeufs',
					'prix':800,
					'image':'https://chefcuisto.com/files/2017/02/pain-fourre-poulet-bbq.jpg'
				},
				{
					'nom':'Pain Poulet sans oeufs',
					'prix':800,
					'image': "https://via.placeholder.com/800x500/.png"
				},


		]
"""