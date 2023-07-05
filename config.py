# DO NOT ADD THIS TO VCS FOR REAL CODE
class Config:
    """
    Use this class to share any default attributes with any subsequent
    classes that inherit from Config.
    """

    DEBUG = False
    TESTING = False

    # Only required when using the session object
    # Generated with secrets.token_urlsafe(16)
    SECRET_KEY = "IM2qjswlx6KM44g46TFE3A"


class ProductionConfig(Config):
    """
    This class will inherit any attributes from the parent Config class.
    Use this class to define production configuration atrributes, such
    as database usernames, passwords, server specific files & directories etc.
    """

    pass


class DevelopmentConfig(Config):
    """
    This class will inherit any attributes from the parent Config class.
    Use this class to define development configuration atrributes, such
    as local database usernames, passwords, local specific files & directories etc.
    """

    DEBUG = True
