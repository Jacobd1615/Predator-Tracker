class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:240179@localhost/animal_db"
    DEBUG = True
    SECRET_KEY = "x"


class TestingConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///testing.db"
    DEBUG = True
    CACHE_TYPE = "SimpleCache"


class ProductionConfig:
    pass
