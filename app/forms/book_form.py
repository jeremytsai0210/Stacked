from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, URL, NumberRange

class BookForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    author = StringField('Author', validators=[InputRequired()])
    description = TextAreaField('Description')
    genre = SelectField('Genre', validators=[InputRequired()], choices=
                        [
                            ('FICTION'), 
                            ('NON_FICTION'),
                            ('FANTASY'),
                            ('SCIENCE_FICTION'),
                            ('MYSTERY'),
                            ('HORROR'),
                            ('ROMANCE'),
                            ('THRILLER'),
                            ('HISTORICAL_FICTION'),
                            ('BIOGRAPHY'),
                            ('AUTOBIOGRAPHY'),
                            ('SELF_HELP'),
                            ('COOKBOOK'),
                            ('POETRY'),
                            ('GRAPHIC_NOVEL'),
                            ('COMIC_BOOK'),
                            ('OTHER')
                        ], default='FICTION')
    cover_image = StringField('Cover Image URL', validators=[URL(message='Invalid URL')])
    total_copies = IntegerField('Total Copies', validators=[NumberRange(min=1, message='Must be at least 1')])
    available_copies = IntegerField('Available Copies', validators=[NumberRange(min=0, message='Must be 0 or more')])
    published_year = IntegerField('Published Year', validators=[NumberRange(min=1000, max=2025, message='Enter a valid year')])