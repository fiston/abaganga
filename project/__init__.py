# project/__init__.py


#################
#### imports ####
#################

import os

from flask import Flask, render_template
from flask.ext.bcrypt import Bcrypt
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail

################
#### config ####
################


app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('project.config.DevelopmentConfig')

####################
#### extensions ####
####################

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)

####################
#### blueprints ####
####################

from project.main.views import main_blueprint
from project.user.views import user_blueprint
from project.profile.views import profile_blueprint
from project.payment.views import payment_blueprint
from project.meeting.views import registration_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(payment_blueprint)
app.register_blueprint(registration_blueprint)

####################
#### flask-login ####
####################

from project.user.models import User

login_manager.login_view = "user.login"
login_manager.login_message_category = "danger"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


########################
#### error handlers ####
########################

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
