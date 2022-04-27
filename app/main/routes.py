from flask import render_template, request, flash
from flask_login import login_required

from app import db
from app.models import User, Role
from app.main import bp


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]

            user = User(username=username, email=email)

            db.session.add(user)

            user.set_password(password)

            user.roles = [Role.query.get(int(request.form["option"]))]

            db.session.commit()

            flash(f'El usuario {user.username} fue creado exitosamente!')

        except:
            flash(f'Hubo un problema creando el usuario, intente mas tarde...!')

    return render_template("register.html", title="Registro")


@bp.route("/", methods=["GET", "POST"])
@login_required
def landing():
    return render_template("form.html", title="Reportes")
