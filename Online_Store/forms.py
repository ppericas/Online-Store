"""
En este script definiremos las diferentes clases que definirán nuestros formularios.

Aunque a simple vista parezca que deberiamos emplear funciones, flask-wtf nos obliga a emplear clases. Los motivos serían:
1. Orientación a Objetos: Las clases encapsulan lógica y datos relacionados con formularios, siguiendo un enfoque orientado a objetos.
2. Reutilización: Las clases de formularios permiten crear instancias reutilizables para diferentes partes de la aplicación.
3. Extensibilidad: Facilita la extensión y modificación de formularios al heredar y modificar clases existentes.
"""


# Importaciones necesarias desde Flask-WTF y WTForms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

"""En el nuevo formulario de login trabajaremos con booleamos"""
from wtforms import BooleanField

# Definición de la clase para el formulario de registro
class SignupForm(FlaskForm):
    # Campos del formulario con etiquetas y validadores
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')  # Botón de envío del formulario
'''
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')
    '''