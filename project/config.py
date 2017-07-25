# project/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    SECURITY_TRACKABLE = True

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # mail settings
    # MAIL_SERVER = 'cloud505.unlimitedwebhosting.co.uk'
    # MAIL_PORT = 465
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True

    # # gmail authentication
    MAIL_USERNAME = 'ngezahayo@gmail.com'
    MAIL_PASSWORD = 'NyiJeanne@09/19'
    #
    # # mail accounts
    MAIL_DEFAULT_SENDER = 'ngezahayo@gmail.com'

    # personal mail authentication
    # MAIL_USERNAME = 'do-not-reply@rwandapaeds.rw'
    # MAIL_PASSWORD = 'Admin@123@'

    # mail accounts
    # MAIL_DEFAULT_SENDER = 'do-not-reply@rwandapaeds.rw'


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    WTF_CSRF_ENABLED = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:NiOrla17@localhost/membership_system'
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
    DEBUG_TB_ENABLED = False
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'
