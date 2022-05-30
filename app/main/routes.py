from datetime import datetime

from flask import render_template, request, flash
from flask_login import login_required, current_user

from app import db
from app.decorators import requires_access_level
from app.models import Candidate, CandidateWorkExperience, CandidateEducation, User, CandidateSkills, \
    CandidateLanguages, CandidateJobInterests
from app.main import bp

ACCESS = {'admin': 2}

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
            end_date = datetime.strptime(request.form["end_date"], "%Y-%m-%d") if request.form.get("end_date",
                                                                                                   None) else None

            candidate_work_experience = CandidateWorkExperience(company_name=request.form["company_name"],
                                                                job_title=request.form["job_title"],
                                                                start_date=datetime.strptime(request.form["start_date"],
                                                                                             "%Y-%m-%d"),
                                                                end_date=end_date,
                                                                currently_working=True if request.form.get(
                                                                    "currently_working", '') == 'on' else False,
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
            yog = datetime.strptime(request.form["year_of_graduation"], "%Y-%m-%d") if request.form.get(
                "year_of_graduation", None) else None

            candidate_education = CandidateEducation(university=request.form["university"],
                                                     degree_name=request.form["degree_name"],
                                                     year_of_graduation=yog,
                                                     currently_enrolled=True if request.form.get("currently_enrolled",
                                                                                                 '') == 'on' else False,
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
    db.session.commit()
    if request.method == "POST":
        try:
            candidate = Candidate.query.filter_by(user_id=current_user.id).first()
            candidate_skill = CandidateSkills(skill_name=request.form["skill_name"],
                                              candidate_id=candidate.id)
            db.session.add(candidate_skill)
            db.session.commit()

            flash(f'La habilidad fue agregada exitosamente!')
        except:
            flash(f'Hubo un problema agregando la habilidad, intente mas tarde...!')

    return render_template("skills_form.html", title="Competencias")


@bp.route("/languages", methods=["GET", "POST"])
@login_required
def languages():
    db.session.commit()
    if request.method == "POST":
        try:
            candidate = Candidate.query.filter_by(user_id=current_user.id).first()
            candidate_language = CandidateLanguages(language_name=request.form["language_name"],
                                                    fluency=request.form["fluency"],
                                                    candidate_id=candidate.id)
            db.session.add(candidate_language)
            db.session.commit()

            flash(f'El idioma fue agregado exitosamente!')
        except:
            flash(f'Hubo un problema agregando el idioma, intente mas tarde...!')

    return render_template("languages_form.html", title="Idiomas")


@bp.route("/job_interest", methods=["GET", "POST"])
@login_required
def job_interest():
    db.session.commit()
    if request.method == "POST":
        try:
            candidate = Candidate.query.filter_by(user_id=current_user.id).first()
            candidate_job_interest = CandidateJobInterests(position_name=request.form["position_name"],
                                                           company_name=request.form["company_name"],
                                                           salary_upper_bound=request.form["salary_upper_bound"],
                                                           salary_lower_bound=request.form["salary_lower_bound"],
                                                           candidate_id=candidate.id)
            db.session.add(candidate_job_interest)
            db.session.commit()

            flash(f'Sus preferencias de empleo fueron agregadas exitosamente!')
        except:
            flash(f'Hubo un problema agregando sus preferencias de empleo, intente mas tarde...!')

    return render_template("job_interest_form.html", title="Preferencias de Empleo")


@bp.route("/candidates", methods=["GET", "POST"])
@login_required
@requires_access_level(ACCESS['admin'])
def candidates():
    user_list = User.query.filter(User.roles.any(name="candidate")).all()
    # check if each user has a candidate otherwise remove from list
    user_list_copy = user_list.copy()
    for user in user_list_copy:
        if not Candidate.query.filter_by(user_id=user.id).first():
            user_list.remove(user)
            print(user.first_name + " removed from list")

    print(user_list)

    return render_template("candidates_page.html", title="Candidatos", user_list=user_list)
