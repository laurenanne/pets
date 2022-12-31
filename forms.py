from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(
        message="You must enter a Name")])
    species = StringField("Species", validators=[InputRequired(
        message="Species cannot be blank"), AnyOf(['dog', 'cat', 'porcupine'])])
    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Must be a valid image url")])
    age = IntegerField("Age", validators=[NumberRange(
        min=0, max=30, message="Must be awhole number between 0 and 30")])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Must be a valid image url")])
    notes = StringField("Notes")
    available = BooleanField("Available")
