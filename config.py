class Config(object):
    """
    Configurações comuns
    """

    DEBUG = True


class DevelopmentConfig(Config):
    """
    Configurações de desenvolvimento
    """

    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Configurações de produção
    """

    DEBUG = False
