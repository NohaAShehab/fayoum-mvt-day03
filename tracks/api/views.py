from flask_restful import Resource, marshal_with
from app.models import db, Track
from app.tracks.api.serializers import track_serilizer
from app.tracks.api.parsers import  track_parser
# views class based

class TrackList(Resource):
    @marshal_with(track_serilizer)
    def get(self):
        tracks  = Track.query.all()
        return tracks # model_object

    @marshal_with(track_serilizer)
    def post(self):
        #create new object ??
        track_data = track_parser.parse_args()
        track = Track(**track_data)
        db.session.add(track)
        db.session.commit()
        return track, 201