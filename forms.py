from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp


class AddCaronaForm(Form):
    local_saida = StringField(
        'Local de Saída',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9\s+]+$',
                message=("Local Não Encontrado")
            )
        ])
    local_chegada = StringField(
        'Local de Entrada',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9\s+]+$',
                message=("Local Não Encontrado")
            )
        ])
