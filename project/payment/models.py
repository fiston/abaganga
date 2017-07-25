# project/models.py
from project import db
from project.uuid_gen import id_column


class Payment(db.Model):
    id = id_column()
    email = db.Column(db.String(255), unique=False, nullable=False)
    names = db.Column(db.String(255), unique=False, nullable=False)
    cardNumber = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    object_payment = db.Column(db.String(255), unique=False, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, names, card_number, phone, amount, object_payment, status=False):
        self.names = names
        self.email = email
        self.cardNumber = card_number
        self.phone = phone
        self.amount = amount
        self.object_payment = object_payment
        self.status = status
