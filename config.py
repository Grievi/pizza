from flask import config
import os

class Config:
    SQLALCHEMY_DATABASE_URI=('postgresql+psycopg2://moringa:access@localhost/pizzashop')
    SQLALCHEMY_TRACK_MODIFICATIONS =False

class DevConfig(Config):

    DEBUG=True

config_options={
  "development":DevConfig
}
