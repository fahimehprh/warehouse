import os


class BaseConfig:
    DEBUG = False

    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'warehouse')
    POSTGRES_PASS = os.environ.get('POSTGRES_PASS', 'warehouse')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'warehouse')

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@'
        f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    )


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = False
