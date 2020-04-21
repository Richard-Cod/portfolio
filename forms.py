from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField , IntegerField,SelectField,TextAreaField,TextField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,required ,length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ContactForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired("Ce champ est requis")])
    email = StringField('email', validators=[DataRequired("Ce champ est requis"),Email("Ce mail est invalide")])
    sujet = StringField('sujet', validators=[DataRequired("Ce champ est requis")])
    message = TextAreaField(u'Message', validators=[DataRequired("Ce champ est requis")])



