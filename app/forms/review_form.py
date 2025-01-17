from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange


class ReviewForm(FlaskForm):
    review_text = StringField('Review Text', validators=[InputRequired()])
    stars = IntegerField('Stars', validators=[NumberRange(min=1, max=5, message='Must be between 1 and 5')])