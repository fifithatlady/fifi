#!/usr/bin/python3

import os

class Config:
    """Base configuration class"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development configuration class"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'

class ProductionConfig(Config):
    """Production configuration class"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(Config):
    """Testing configuration class"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
