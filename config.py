import os 

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ="https://api.themoviedb.org/3/movie/{}?api_key={}"
    MOVIE_API_KEY = "48044421b8e8df69b5776ae46e6b4237"
    SECRET_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ODA0NDQyMWI4ZThkZjY5YjU3NzZhZTQ2ZTZiNDIzNyIsInN1YiI6IjYzNjJkM2EzNWNhNzA0MDA3YWMxNWY3NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Do1LgBQtxDPcX35epTESA5KqYi_k99P0RhEfyuwerd4"
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://collins:11946@localhost/watchlist"
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "deveshvitap@gmail.com"
    MAIL_PASSWORD = "prajwal"

    # simplemde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    """
    Test configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://collins:11946@localhost/watchlist_test"

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://collins:11946@localhost/watchlist"
    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}