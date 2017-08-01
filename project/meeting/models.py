# project/models.py


import datetime

from sqlalchemy.orm import relationship

from project import db, bcrypt


class Registration(db.Model):
    __tablename__ = "registration"

    registration_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    telephone = db.Column(db.String(255), nullable=False)
    rmdc_number = db.Column(db.String(255), nullable=True)
    validity = db.Column(db.Boolean, nullable=True, default=False)

    def __init__(self, title, firstName, lastName, email, telephone, occupation, validity):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.telephone = telephone
        self.rmdc_number = occupation
        self.validity = validity

    def __repr__(self):
        return '<firstName {}'.format(self.firstName)
