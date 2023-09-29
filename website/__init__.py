from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate

db = SQLAlchemy()
DB_NAME = "freight_description.db"

def create_app():
    app = Flask(__name__,template_folder='website_temp')
    app.config['SECRET_KEY'] = 'theriyumla'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_NOTIFICTIONS']=False
    db.init_app(app)

    from .views import views
    from .flights import flights 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(flights, url_prefix='/')
    

    from .models import Freightproperty
    
    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        migrate = Migrate(app, db)
        db.create_all(app=app)
        print('Created Database')