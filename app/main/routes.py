from datetime import datetime

from flask import render_template, request, flash, redirect, url_for, Response, jsonify
from flask_login import login_required, current_user

from app import db
from app.decorators import requires_access_level
from app.models import Candidate, CandidateWorkExperience, CandidateEducation, User, CandidateSkills, \
    CandidateLanguages, CandidateJobInterests
from app.main import bp

ACCESS = {'admin': 2}


@bp.route("/work_experience", methods=["GET", "POST"])
@login_required
def work_experience():
    db.session.commit()
    if request.method == "POST":
        try:
            if request.form['edit_id']:
                candidate_work_experience = CandidateWorkExperience.query.filter_by(id=request.form['edit_id']).first()
                candidate_work_experience.company_name = request.form['company_name']
                candidate_work_experience.job_title = request.form['job_title']
                candidate_work_experience.start_date = datetime.strptime(request.form['start_date'], "%Y-%m-%d")
                candidate_work_experience.end_date = datetime.strptime(request.form['end_date'], "%Y-%m-%d") if \
                    request.form['end_date'] else None
                candidate_work_experience.currently_working = True if request.form.get('currently_working',
                                                                                       '') == 'on' else False
                db.session.commit()
                flash(f'La experiencia laboral fue actualizada exitosamente!');
            else:

                candidate = Candidate.query.filter_by(user_id=current_user.id).first()
                end_date = datetime.strptime(request.form["end_date"], "%Y-%m-%d") if request.form.get("end_date",
                                                                                                       None) else None

                candidate_work_experience = CandidateWorkExperience(company_name=request.form["company_name"],
                                                                    job_title=request.form["job_title"],
                                                                    start_date=datetime.strptime(
                                                                        request.form["start_date"],
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

    work_experience_list = CandidateWorkExperience.query.filter_by(candidate_id=current_user.candidate.id).all()

    return render_template("work_experience_form.html", title="Experiencia Laboral",
                           work_experience_list=work_experience_list)


@bp.route("/delete_work_experience", methods=["DELETE"])
@login_required
def delete_work_experience():
    try:
        candidate_work_experience = CandidateWorkExperience.query.filter_by(id=request.form['id']).first()
        db.session.delete(candidate_work_experience)
        db.session.commit()
        flash(f'La experiencia laboral fue eliminada exitosamente!');
        return Response(status=200);
    except:
        flash(f'Hubo un problema eliminando la experiencia laboral, intente mas tarde...!');
        return Response(status=500);


@bp.route("/get_work_experience", methods=["GET"])
@login_required
def get_work_experience():
    try:
        print(request.args['id'])
        candidate_work_experience = CandidateWorkExperience.query.filter_by(id=request.args['id']).first()
        new_dict = {
            'id': candidate_work_experience.id,
            'company_name': candidate_work_experience.company_name,
            'job_title': candidate_work_experience.job_title,
            'start_date': candidate_work_experience.start_date.strftime("%Y-%m-%d"),
            'end_date': candidate_work_experience.end_date.strftime(
                "%Y-%m-%d") if candidate_work_experience.end_date else '',
            'currently_working': candidate_work_experience.currently_working
        }
        return jsonify(new_dict)

    except:
        return Response(status=500);


@bp.route("/education", methods=["GET", "POST"])
@login_required
def education():
    db.session.commit()
    if request.method == "POST":
        try:
            if request.form['edit_id']:
                candidate_education = CandidateEducation.query.filter_by(id=request.form['edit_id']).first()
                candidate_education.university = request.form['university']
                candidate_education.degree_name = request.form['degree_name']
                candidate_education.year_of_graduation = datetime.strptime(request.form["year_of_graduation"],
                                                                           "%Y-%m-%d") if request.form.get(
                    "year_of_graduation", None) else None
                candidate_education.currently_enrolled = True if request.form.get("currently_enrolled",
                                                                                  '') == 'on' else False
                db.session.commit()
                flash(f'La educación fue actualizada exitosamente!')
            else:

                candidate = Candidate.query.filter_by(user_id=current_user.id).first()
                yog = datetime.strptime(request.form["year_of_graduation"], "%Y-%m-%d") if request.form.get(
                    "year_of_graduation", None) else None

                candidate_education = CandidateEducation(university=request.form["university"],
                                                         degree_name=request.form["degree_name"],
                                                         year_of_graduation=yog,
                                                         currently_enrolled=True if request.form.get(
                                                             "currently_enrolled",
                                                             '') == 'on' else False,
                                                         candidate_id=candidate.id)

                db.session.add(candidate_education)
                db.session.commit()

                flash(f'La experiencia académica fue actualizada exitosamente!')
        except:
            flash(f'Hubo un problema actualizando la experiencia académica, intente mas tarde...!')

    education_list = CandidateEducation.query.filter_by(candidate_id=current_user.candidate.id).all()

    return render_template("education_form.html", title="Experiencia Académica", education_list=education_list)


@bp.route("/delete_education", methods=["DELETE"])
@login_required
def delete_education():
    try:
        candidate_education = CandidateEducation.query.filter_by(id=request.form['id']).first()
        db.session.delete(candidate_education)
        db.session.commit()
        flash(f'La experiencia académica fue eliminada exitosamente!');
        return Response(status=200);
    except:
        flash(f'Hubo un problema eliminando la experiencia académica, intente mas tarde...!');
        return Response(status=500);


@bp.route("/get_education", methods=["GET"])
@login_required
def get_education():
    try:
        candidate_education = CandidateEducation.query.filter_by(id=request.form['id']).first()
        education = {
            'id': candidate_education.id,
            'university': candidate_education.university,
            'degree_name': candidate_education.degree_name,
            'year_of_graduation': candidate_education.year_of_graduation.strftime(
                "%Y-%m-%d") if candidate_education.year_of_graduation else None,
            'currently_enrolled': candidate_education.currently_enrolled
        }
        return jsonify(education)
    except:
        return Response(status=500);


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

    skill_list = CandidateSkills.query.filter_by(candidate_id=current_user.candidate.id).all()
    return render_template("skills_form.html", title="Competencias", skill_list=skill_list)


@bp.route("/delete_skill", methods=["DELETE"])
@login_required
def delete_skill():
    try:
        candidate_skill = CandidateSkills.query.filter_by(id=request.form['id']).first()
        db.session.delete(candidate_skill)
        db.session.commit()
        flash(f'La habilidad fue eliminada exitosamente!');
        return Response(status=200);
    except:
        flash(f'Hubo un problema eliminando la habilidad, intente mas tarde...!');
        return Response(status=500);


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

    language_list = CandidateLanguages.query.filter_by(candidate_id=current_user.candidate.id).all()

    return render_template("languages_form.html", title="Idiomas", language_list=language_list)


@bp.route("/delete_language", methods=["DELETE"])
@login_required
def delete_language():
    try:
        candidate_language = CandidateLanguages.query.filter_by(id=request.form['id']).first()
        db.session.delete(candidate_language)
        db.session.commit()
        flash(f'El idioma fue eliminado exitosamente!');
        return Response(status=200);
    except:
        flash(f'Hubo un problema eliminando el idioma, intente mas tarde...!');
        return Response(status=500);


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

    job_interest_list = CandidateJobInterests.query.filter_by(candidate_id=current_user.candidate.id).all()

    return render_template("job_interest_form.html", title="Preferencias de Empleo",
                           job_interest_list=job_interest_list)


@bp.route("/delete_job_interest", methods=["DELETE"])
@login_required
def delete_job_interest():
    try:
        candidate_job_interest = CandidateJobInterests.query.filter_by(id=request.form['id']).first()
        db.session.delete(candidate_job_interest)
        db.session.commit()
        flash(f'Sus preferencias de empleo fueron eliminadas exitosamente!');
        return Response(status=200);
    except:
        flash(f'Hubo un problema eliminando sus preferencias de empleo, intente mas tarde...!');
        return Response(status=500);


@bp.route("/candidates", methods=["GET", "POST"])
@login_required
@requires_access_level(ACCESS['admin'])
def candidates():
    user_list = User.query.filter(User.roles.any(name="candidate")).all()
    user_list_copy = user_list.copy()
    for user in user_list_copy:
        if not Candidate.query.filter_by(user_id=user.id).first():
            user_list.remove(user)
            print(user.first_name + " removed from list")

    print(user_list)

    return render_template("candidates_page.html", title="Candidatos", user_list=user_list)
