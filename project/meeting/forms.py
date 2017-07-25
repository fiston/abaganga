# project/user/forms.py


from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length


class RegistrationForm(Form):
    title = SelectField('title', validators=[DataRequired("Please select a Title")],
                        choices=[('MD', 'Medical Doctor (MD)'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'),
                                 ('Phd', 'Phd.')])
    firstName = StringField('firstName', validators=[DataRequired(), Length(min=6, max=25)])
    lastName = StringField('lastName', validators=[DataRequired(), Length(min=6, max=25)])
    telephone = StringField('telephone', validators=[DataRequired(), Length(min=2, max=25)])
    occupation = StringField('occupation', validators=[DataRequired(), Length(min=2, max=25)])
