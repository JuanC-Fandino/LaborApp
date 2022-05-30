from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from werkzeug.urls import url_parse
from app.auth import bp
from app.models import User, Role, Candidate
from app.auth.forms import LoginForm
from app import db


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.education'))

    if request.method == "POST":
        try:
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            phone = request.form["phone"]

            password = request.form["password"]
            password_confirm = request.form["password_confirm"]

            if password != password_confirm:
                flash(f'Las contraseñas no coinciden!')
                return render_template("register_form.html", title="Registro")

            user = User(first_name=first_name, last_name=last_name, email=email, phone=phone)

            db.session.add(user)

            user.set_password(password)

            user.roles = [Role.query.get(1)]

            new_candidate = Candidate(user_id=user.id)

            db.session.add(new_candidate)

            db.session.commit()

            flash(f'¡Bienvenido {user.first_name + " " + user.last_name}! Tu cuenta fue creada con éxito.')

            login_user(user)

            return redirect(url_for('main.education'))

        except:
            flash(f'Hubo un problema creando el usuario, intente mas tarde...!')

    return render_template("register.html", title="Registro")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.education'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('El usuario o la contraseña son incorrectos')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.education')
        return redirect(next_page)
    return render_template('auth/login.html', title='Iniciar Sesión', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
