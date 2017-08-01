# project/profile/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask.ext.login import login_required, current_user

from project import db
from project.decorators import check_confirmed, check_is_admin

################
#### config ####
################
from project.payment import client
from project.payment.forms import PaymentForm
from project.payment.models import Payment

payment_blueprint = Blueprint('payment', __name__, )


################
#### routes ####
################

@payment_blueprint.route('/payment', methods=['GET', 'POST'])
@login_required
@check_confirmed
def payment_add():
    form = PaymentForm(request.form)
    if form.validate_on_submit():
        payment = Payment(
            names=form.names.data,
            email=form.email.data,
            card_number=form.cardNumber.data,
            phone=form.phone.data,
            amount=form.amount.data,
            object_payment=form.object_payment.data,
            status=False
        )
        client.make_mobile_payment(payment.amount, payment.phone, payment.names)
        db.session.add(payment)
        db.session.commit()
        flash('Your payment has been initialized.', 'success')
        return redirect(url_for("payment.payment_add"))

    return render_template('payment/new_payment.html', form=form)

#
#
# @payment_blueprint.route('/profile_edit/<profile_id>', methods=['GET', 'POST'])
# @login_required
# def profile_edit(profile_id):
#     profile = Profile.query.filter_by(id=profile_id).first()
#     form = ProfileForm(obj=profile)
#     if form.validate_on_submit():
#         profile.bio = form.bio.data,
#         profile.phone = form.phone.data,
#         profile.profile_pic = form.profilePic.data
#         db.session.commit()
#         flash('Your profile has been saved.', 'success')
#         return redirect(url_for("profile.display"))
#     return render_template('profile/register.html', form=form)
#
#
# @payment_blueprint.route('/display', methods=['GET'])
# @login_required
# @check_confirmed
# def display():
#     user = User.query.filter_by(email=current_user.email).first()
#     profile = Profile.query.filter_by(user_id=user.id).first()
#
#     return render_template('profile/profile.html', profile=profile, user=user)
#
#
# @payment_blueprint.route('/list', methods=['GET'])
# @login_required
# @check_confirmed
# @check_is_admin
# def list_all():
#     profiles = Profile.query.all()
#     return render_template('profile/list.html', profiles=profiles)
#
#
# @payment_blueprint.route('/profile_view/<profile_id>', methods=['GET'])
# @login_required
# def profile_view(profile_id):
#     profile = Profile.query.filter_by(id=profile_id).first()
#
#     return render_template('profile/profileView.html', profile=profile)
#
#
# @payment_blueprint.route('/profile_confirm/<profile_id>', methods=['GET'])
# @login_required
# def profile_confirm(profile_id):
#     profile = Profile.query.get(profile_id)
#     user_id = profile.user_id
#     user = User.query.filter_by(id=user_id).first()
#     profile.validity = False
#     db.session.commit()
#     html = render_template('profile/confirmed.html')
#     subject = "Your Membership Has been Confirmed"
#     send_email(user.email, subject, html)
#     flash('Membership has been Confirmed.', 'success')
#     return render_template('profile/profileView.html', profile=profile)
#
#
# @payment_blueprint.route('/profile_delete/<profile_id>', methods=['GET'])
# @login_required
# def profile_delete(profile_id):
#     profile = Profile.query.get(profile_id)
#     user_id = profile.user_id
#     user = User.query.filter_by(id=user_id).first()
#     profile.validity = False
#     db.session.commit()
#     # user = User.query.filter_by(id=profile.user_id).first()
#     html = render_template('profile/revoke.html')
#     subject = "Your Membership Has been revoked"
#     send_email(user.email, subject, html)
#     flash('Membership has been Revoked. An email has been sent to the member', 'danger')
#     return render_template('profile/profileView.html', profile=profile)
