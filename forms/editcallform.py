from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired
from forms.geo_validators import  AddressRequired


class EditCallForm(FlaskForm):
    message = TextAreaField('Сообщение', validators=[DataRequired(message="Поле 'сообщение' не может быть пустым")])
    address = StringField('Адрес происшествия', validators=[DataRequired(message="Поле 'адрес' не может быть пустым"),
                                                            AddressRequired(unique=True)])
    service = RadioField('Служба', choices=[('fire','Пожарная охрана'),('police','Полиция'), ('ambulance','Скорая помощь')])
    status = RadioField('Статус', choices=[('received','Принят'),('serviced','Выполняется'), ('finished','Завершен')])
    submit = SubmitField('Cохранить изменения')
