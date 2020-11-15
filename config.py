import os

class Config(object):
    SECRET_KEY= "Es un secreto, de tu mirada y la mia, un presentimiento xdsxdsxxds"

class DevelopmentConfig(Config):
    DEBUG = True