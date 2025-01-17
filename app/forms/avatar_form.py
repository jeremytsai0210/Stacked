from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, URL


class AvatarForm(FlaskForm):
    avatar_image = StringField('avatar_image', validators=[DataRequired(), URL()])
    description = TextAreaField('description')