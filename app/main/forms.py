from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class PostForm(FlaskForm):
    post = TextAreaField(_l('Напишите что-нибудь'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Отправить'))


class EditProfileForm(FlaskForm):
    username = StringField(_l('Имя пользователя'), validators=[DataRequired()])
    about_me = TextAreaField(_l('Обо мне'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Отправить'))
    
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Пожалуйста, используйте другое имя пользователя')


class MessageForm(FlaskForm):
    message = TextAreaField(_l('Сообщение'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Отправить')