
class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://fayoum:iti@localhost:5432/flask_d3'


config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}