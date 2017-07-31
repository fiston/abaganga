# project/user/forms.py


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ProfileForm(Form):
    bio = StringField('Bio', validators=[DataRequired(), Length(min=6, max=25)])
    profilePic = StringField('Profile Pic', validators=[DataRequired(), Length(min=6, max=25)])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=2, max=25)])
