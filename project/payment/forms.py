# project/user/forms.py


from flask_wtf import Form
from wtforms import StringField, FloatField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length


class CardPaymentForm(Form):
    email = StringField('email', validators=[DataRequired(), Length(min=6, max=25)])
    names = StringField('names', validators=[DataRequired(), Length(min=3, max=45)])
    cardNumber = StringField('cardNumber', validators=[DataRequired(), Length(min=6, max=25)], default="None")
    phone = StringField('phone', validators=[DataRequired(), Length(min=2, max=25)])
    amount = IntegerField('Amount', default=1, validators=[DataRequired("This field is required")])
    object_payment = SelectField('objectPayment', validators=[DataRequired("Please select the reason for payment")],
                                 choices=[('membership', 'Annual Membership'), ('donation', 'Donation'),
                                          ('meeting', 'Meeting Registration')])


