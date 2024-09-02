from flask import request, render_template, redirect, url_for
from app.students import  student_blueprint
from app.models import Student, db, Track


@student_blueprint.route('', endpoint='index')
def index():
    students = Student.query.all()
    return render_template("students/index.html", students=students)


@student_blueprint.route("/create", methods=["GET", "POST"], endpoint="create")
def create():
    tracks = Track.query.all()
    if request.method == "POST":
        print(request.form['track_id'])
        student = Student(name=request.form["name"], grade=request.form["grade"],image=request.form["image"],
                          track_id=request.form["track_id"])
        db.session.add(student)
        db.session.commit()
        # return "addedd"
        return redirect(student.show_url)

    return  render_template("students/create.html", tracks=tracks)


@student_blueprint.route("/<int:id>",  endpoint="show")
def show(id):
    student = db.get_or_404(Student, id)
    # track = db.get_or_404(Track, student.track_id)
    return render_template("students/show.html", student=student)




@student_blueprint.route("/<int:id>/delete", endpoint="delete", methods=["POST"])
def delete(id):
    student = db.get_or_404(Student, id)
    db.session.delete(student)
    db.session.commit()
    return  redirect(url_for("students.index"))




from app.students.forms import StudentForm

###
@student_blueprint.route("/form/create", endpoint="form_create", methods=["POST", "GET"])
def create_student():
    form  = StudentForm()
    # form.track_id =  [(t.id, t.name) for t in Track.query.all()]
    if request.method=='POST':
        if form.validate_on_submit():
            print(request.form)
            student = Student(name=request.form["name"], grade=request.form["grade"],image=request.form["image"],
                              track_id=request.form["track_id"])
            db.session.add(student)
            db.session.commit()
            return redirect(student.show_url)

    return  render_template("students/forms/create.html", form=form)





