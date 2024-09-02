from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_restful import Resource, Api


from app.config import config_options
from app.models import  db


def create_app(config_name='prd'):
    app = Flask(__name__)
    current_config = config_options[config_name]
    app.config.from_object(current_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI

    ## define place for uploads


    db.init_app(app)

    migrate = Migrate(app, db)

    bootstrap = Bootstrap5(app)
    api = Api(app)



    # we need db, migration


    # app we need to register blueprint ?
    from app.students import  student_blueprint
    app.register_blueprint(student_blueprint)
    from app.tracks import track_blueprint
    app.register_blueprint(track_blueprint)


    ## generate urls for API
    from app.students.api.views import  StudentList, StudentResource
    api.add_resource(StudentList, '/api/students')
    api.add_resource(StudentResource, '/api/students/<int:id>')

    ####
    from app.tracks.api.views import TrackList
    api.add_resource(TrackList, '/api/tracks')

    return app
