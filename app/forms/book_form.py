from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, URL, NumberRange, ValidationError


def validate_available_copies(form, field):
        if form.total_copies.data is None:
            raise ValidationError('Total copies must be specified before validating available copies.')
        if field.data > form.total_copies.data:
            raise ValidationError('Available copies cannot exceed total copies.')
class BookForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    author = StringField('Author', validators=[InputRequired()])
    description = TextAreaField('Description')
    genre = SelectField('Genre', validators=[InputRequired()], choices=
                        [
                            ('FICTION', 'Fiction'),
                            ('NON_FICTION', 'Non-fiction'),
                            ('FANTASY', 'Fantasy'),
                            ('SCIENCE_FICTION', 'Science Fiction'),
                            ('MYSTERY', 'Mystery'),
                            ('HORROR', 'Horror'),
                            ('ROMANCE', 'Romance'),
                            ('THRILLER', 'Thriller'),
                            ('HISTORICAL_FICTION', 'Historical Fiction'),
                            ('BIOGRAPHY', 'Biography'),
                            ('AUTOBIOGRAPHY', 'Autobiography'),
                            ('SELF_HELP', 'Self-Help'),
                            ('COOKBOOK', 'Cookbook'),
                            ('POETRY', 'Poetry'),
                            ('GRAPHIC_NOVEL', 'Graphic Novel'),
                            ('COMIC_BOOK', 'Comic Book'),
                            ('OTHER', 'Other')
                        ], default='FICTION')
    cover_image = StringField('Cover Image URL', validators=[URL(message='Invalid URL')])
    total_copies = IntegerField('Total Copies', default=1, validators=[NumberRange(min=1, message='Must be at least 1')])
    available_copies = IntegerField('Available Copies', default=0, validators=[
        NumberRange(min=0, message='Must be 0 or more'),
        validate_available_copies
    ])
    published_year = IntegerField('Published Year', validators=[NumberRange(min=1000, max=2025, message='Enter a valid year')])