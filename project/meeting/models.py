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
    telephone = db.Column(db.String(255), nullable=False)
    occupation = db.Column(db.String(255), nullable=False)
    validity = db.Column(db.Boolean, nullable=True, default=False)


    def __init__(self, title, firstName, lastName, telephone, occupation, validity):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.telephone = telephone
        self.occupation = occupation
        self.validity = validity

    def __repr__(self):
        return '<firstName {}'.format(self.firstName)
