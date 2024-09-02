
from flask_restful import reqparse

track_parser = reqparse.RequestParser()

track_parser.add_argument('name', type=str, required=True)
