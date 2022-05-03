from datetime import datetime

from flask import render_template, request, flash
from flask_login import login_required, current_user

from app import db
from app.models import Candidate, CandidateWorkExperience, CandidateEducation
from app.main import bp


@bp.route("/", methods=["GET", "POST"])
@login_required
def landing():
    return render_template("education_form.html", title="Experiencia Académica")


@bp.route("/work_experience", methods=["GET", "POST"])
@login_required
def work_experience():
    db.session.commit()
    if request.method == "POST":
        try:
            candidate = Candidate.query.filter_by(user_id=current_user.id).first()
            end_date = datetime.strptime(request.form["end_date"], "%Y-%m-%d") if request.form.get("end_date", None) else None

            candidate_work_experience = CandidateWorkExperience(company_name=request.form["company_name"],
                                                                job_title=request.form["job_title"],
                                                                start_date=datetime.strptime(request.form["start_date"],
                                                                                             "%Y-%m-%d"),
                                                                end_date=end_date,
                                                                currently_working=True if request.form.get("currently_working", '') == 'on' else False,
                                                                candidate_id=candidate.id)

            db.session.add(candidate_work_experience)
            db.session.commit()

            flash(f'La experiencia laboral fue actualizada exitosamente!')
        except:
            flash(f'Hubo un problema actualizando la experiencia laboral, intente mas tarde...!')

    return render_template("work_experience_form.html", title="Experiencia Laboral")


@bp.route("/education", methods=["GET", "POST"])
@login_required
def education():
    db.session.commit()
    if request.method == "POST":
        try:
            candidate = Candidate.query.filter_by(user_id=current_user.id).first()
            yog = datetime.strptime(request.form["year_of_graduation"], "%Y-%m-%d") if request.form.get("year_of_graduation", None) else None

            candidate_education = CandidateEducation(university=request.form["university"],
                                                     degree_name=request.form["degree_name"],
                                                     year_of_graduation=yog,
                                                     currently_enrolled=True if request.form.get("currently_enrolled", '') == 'on' else False,
                                                     candidate_id=candidate.id)

            db.session.add(candidate_education)
            db.session.commit()

            flash(f'La experiencia académica fue actualizada exitosamente!')
        except:
            flash(f'Hubo un problema actualizando la experiencia académica, intente mas tarde...!')

    return render_template("education_form.html", title="Experiencia Académica")


@bp.route("/skills", methods=["GET", "POST"])
@login_required
def skills():
    return render_template("skills_form.html", title="Competencias")


@bp.route("/candidates", methods=["GET", "POST"])
@login_required
def candidates():
    return render_template("candidates_page.html", title="Candidatos")
