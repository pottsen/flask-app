import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False
    # DATABASE_URL = 'postgresql://qvfvcvfuuvbxlv:9218667034f957f717746aec3050317d19156bcd4180221086103bf248cc1f71@ec2-18-235-154-252.compute-1.amazonaws.com:5432/d1ih6l1fogc1qu'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
