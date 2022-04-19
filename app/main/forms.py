from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import InputRequired, Length

class FormImoveis(FlaskForm):
    logradouro = StringField('Logradouro', validators=[InputRequired()])
    cep = IntegerField('CEP', validators=[InputRequired()])
    bairro = StringField('Bairro', validators=[InputRequired()])
    cidade = StringField('Cidade', validators=[InputRequired()])

class FormProprietarios(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired()])
    data_de_nascimento = DateField('Data de Nascimento',
                                   format='%d/%m/%Y',
                                   validators=[InputRequired()])

class FormInquilinos(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired()])
    data_de_nascimento = DateField('Data de Nascimento',
                                   format='%d/%m/%Y',
                                   validators=[InputRequired()])

class FormAlugueis(FlaskForm):
    imovel = IntegerField('Id do Imovel', validators=[InputRequired()])
    proprietario = IntegerField('Id do Proprietario', validators=[InputRequired()])

class FormContratos(FlaskForm):
    aluguel = IntegerField('Id do Aluguel', validators=[InputRequired()])
    inquilino = IntegerField('Id do Inquilino', validators=[InputRequired()])
