from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BandForm(FlaskForm):
    band_name = StringField("Task Description", validators=[DataRequired()])
    submit = SubmitField("Add Band")