from flask_restful import reqparse


student_parser = reqparse.RequestParser()

student_parser.add_argument("name", required=True, type=str, help="Name is required")
student_parser.add_argument("image", required=True, type=str, help="Image is required")
student_parser.add_argument("grade", required=True, type=int, help="Grade is required")
student_parser.add_argument("track_id", required=True, type=int, help="Track ID is required")