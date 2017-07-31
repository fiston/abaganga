# project/user/forms.py


from flask_wtf import Form
from wtforms import StringField, FloatField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length


class CardPaymentForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=25)])
    names = StringField('Names', validators=[DataRequired(), Length(min=3, max=45)])
    # cardNumber = StringField('Card Number', validators=[DataRequired(), Length(min=6, max=25)], default="None")
    phone = StringField('Phone', validators=[DataRequired(), Length(min=2, max=25)])
    amount = IntegerField('Amount', default=1, validators=[DataRequired("This field is required")])
    object_payment = SelectField('Payment Service', validators=[DataRequired("Please select the reason for payment")],
                                 choices=[('membership', 'Annual Membership'), ('donation', 'Donation'),
                                          ('meeting', 'Meeting Registration')])


