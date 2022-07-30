import os


class Base:
    DEBUG = False
    TESTING = False
    SSL_REDIRECT = False
    MONGO_URI = None
    SECRET_KEY = os.getenv("SECRET_KEY", "hard-to-guess")


class Production(Base):
    FLASK_CONFIG = "production"
    MONGO_URI = os.getenv("MONGO_URI")


class Development(Base):
    FLASK_CONFIG = "development"
    DEBUG = True
    MONGO_URI = os.getenv("MONGO_URI")


class Test(Base):
    TESTING = True


config = {
    "production": Production,
    "development": Development,
    "testing": Test,
}
