from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length
from app.models import Track, db


class StudentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(2, 40)])
    # image= StringField("Image")
    image= FileField("Image", validators=[DataRequired()]) # this will include in form tag enctype=multi-part form ?
    grade = IntegerField("Grade")

    track_id = SelectField("Track", validators=[DataRequired()], choices=[])
    submit = SubmitField("Save new Student")

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # while creating object from form --> please give me the tracks
        self.track_id.choices = [(t.id, t.name) for t in Track.query.all()]