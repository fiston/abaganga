# project/registration/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask.ext.login import login_required, current_user

from project import db
from project.decorators import check_confirmed, check_is_admin
from project.email import send_email
from project.meeting.models import Registration
from project.profile.models import Profile
from project.user.models import User
from .forms import RegistrationForm

################
#### config ####
################

registration_blueprint = Blueprint('registration', __name__, )


################
#### routes ####
################

@registration_blueprint.route('/registrationAdd', methods=['GET', 'POST'])
# @login_required
# @check_confirmed
def registration_add():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        registration = Registration(

            title=form.title.data,
            firstName=form.firstName.data,
            lastName=form.lastName.data,
            telephone=form.telephone.data,
            occupation=form.occupation.data,
            validity=False,
        )
        db.session.add(registration)
        db.session.commit()
        flash('Your registration has been saved.', 'success')
        return redirect(url_for("registration.display"))
    elif form.is_submitted():
        flash(form.errors, 'danger')
    return render_template('registration/register.html', form=form)


@registration_blueprint.route('/registration_edit/<registration_id>', methods=['GET', 'POST'])
@login_required
def registration_edit(registration_id):
    registration = Registration.query.filter_by(id=registration_id).first()
    form = RegistrationForm(obj=registration)
    if form.validate_on_submit():
        registration.firstName = form.firsName.data,
        registration.lastName = form.lastName.data,
        registration.telephone = form.telephone.data,
        registration.occupation = form.occupation.data
        db.session.commit()
        flash('Your registration has been saved.', 'success')
        return redirect(url_for("registration.display"))
    return render_template('registration/register.html', form=form)


@registration_blueprint.route('/display_result', methods=['GET'])
def display():
    # registration = Registration.query.filter_by(registration_id=id).first()
    return render_template('registration/after_saving.html')


@registration_blueprint.route('/list', methods=['GET'])
@login_required
@check_confirmed
@check_is_admin
def list_all():
    registrations = Registration.query.all()
    return render_template('registration/list.html', registrations=registrations)


@registration_blueprint.route('/registration_view/<registration_id>', methods=['GET'])
@login_required
def registration_view(registration_id):
    registration = Registration.query.filter_by(id=registration_id).first()

    return render_template('registration/registrationView.html', registration=registration)


@registration_blueprint.route('/registration_confirm/<registration_id>', methods=['GET'])
@login_required
def registration_confirm(registration_id):
    registration = Registration.query.get(registration_id)
    registration.validity = False
    db.session.commit()
    html = render_template('registration/confirmed.html')
    subject = "Your Membership Has been Confirmed"
    send_email(registration.email, subject, html)
    flash('Membership has been Confirmed.', 'success')
    return render_template('registration/registrationView.html', registration=registration)


@registration_blueprint.route('/registration_delete/<registration_id>', methods=['GET'])
@login_required
def registration_delete(registration_id):
    registration = Registration.query.get(registration_id)
    registration.validity = False
    db.session.commit()
    # user = User.query.filter_by(id=profile.user_id).first()
    html = render_template('registration/revoke.html')
    subject = "Your Membership Has been revoked"
    send_email(registration.email, subject, html)
    flash('Membership has been Revoked. An email has been sent to the member', 'danger')
    return render_template('registration/registrationView.html', registration=registration)
