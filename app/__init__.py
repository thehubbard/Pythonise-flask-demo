from flask import Flask


app = Flask(__name__)


if app.debug:
    app.config.from_object("config.DevelopmentConfig")

else:
    app.config.from_object("config.ProductionConfig")


from app import views
