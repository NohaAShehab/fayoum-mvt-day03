

from flask import Blueprint

# name --> url name
student_blueprint = Blueprint('students', __name__, url_prefix='/students')


from app.students import  views