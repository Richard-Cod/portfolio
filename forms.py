from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField , IntegerField,SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
"""

class CategorieForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    type_id = SelectField(u'Type', coerce=int)


class TypeForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])


class OperationForm(FlaskForm):
    montant = IntegerField('Montant', validators=[DataRequired()])

class PlatForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    prix = IntegerField('prix', validators=[DataRequired()])
    categorie_id = SelectField(u'Categorie', coerce=int)





class CommandeForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    prix = IntegerField('prix', validators=[DataRequired()])
    categorie_id = SelectField(u'Categorie', coerce=int)
"""