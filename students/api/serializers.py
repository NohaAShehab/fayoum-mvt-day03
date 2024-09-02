from flask_restful import fields

# i need track id , track name
track_serilizer ={
    "id": fields.Integer,
    "name": fields.String
}


# how to send image with full path
student_serializers = {
    "id": fields.Integer,
    "name":fields.String,
    "image":fields.String,
    "grade":fields.Integer,
    "track_id":fields.Integer,
    "track" :fields.Nested(track_serilizer),
}