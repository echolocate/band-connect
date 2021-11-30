from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BandForm(FlaskForm):
    name = StringField("Band Name", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    submit = SubmitField("Add Band")