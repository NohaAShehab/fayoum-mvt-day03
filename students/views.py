from flask import request, render_template, redirect, url_for
from app.students import  student_blueprint
from app.models import Student, db


@student_blueprint.route('', endpoint='index')
def index():
    students = Student.query.all()
    return render_template("students/index.html", students=students)


@student_blueprint.route("/create", methods=["GET", "POST"], endpoint="create")
def create():
    if request.method == "POST":
        student = Student(name=request.form["name"], grade=request.form["grade"],image=request.form["image"])
        db.session.add(student)
        db.session.commit()
        # return "addedd"
        return redirect(student.show_url)

    return  render_template("students/create.html")


@student_blueprint.route("/<int:id>",  endpoint="show")
def show(id):
    student = db.get_or_404(Student, id)
    return render_template("students/show.html", student=student)




@student_blueprint.route("/<int:id>/delete", endpoint="delete", methods=["POST"])
def delete(id):
    student = db.get_or_404(Student, id)
    db.session.delete(student)
    db.session.commit()
    return  redirect(url_for("students.index"))












