from flask_restful import Resource, Api, marshal_with
from app.models import  db, Student
from app.students.api.serializers import  student_serializers
from app.students.api.parsers import  student_parser
### define classes from views ??

# class create api for resource --> student
# this class contains views for get all student
class StudentList(Resource):
    @marshal_with(student_serializers)
    def get(self):
        # return with all students
        students=  Student.query.all()
        return students, 200

    # save new student
    @marshal_with(student_serializers)
    def post(self):
        # I need to get request data ??
        student_args = student_parser.parse_args() # get request data
        print(student_args)
        student = Student(**student_args) # dict
        db.session.add(student)
        db.session.commit()
        # return "student", 201
        return student, 201


class StudentResource(Resource):
    @marshal_with(student_serializers)
    def get(self,id):
        student = db.get_or_404(Student, id)
        return student, 200

    @marshal_with(student_serializers)
    def put(self,id):
        student = db.get_or_404(Student, id)
        student_args = student_parser.parse_args()
        student.name= student_args['name']
        student.grade= student_args['grade']
        student.image= student_args['image']
        student.track_id= student_args['track_id']
        db.session.add(student)
        db.session.commit()
        return student, 200




    def delete(self,id):
        student = db.get_or_404(Student, id)
        db.session.delete(student)
        db.session.commit()
        return "deleted", 204
