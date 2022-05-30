from functools import wraps
from flask import url_for, redirect, abort
from flask_login import current_user

from app.models import User


def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.is_anonymous:
                return redirect(url_for('login'))

            user = User.query.get(current_user.id)

            if not user.allowed(access_level):
                abort(403)

            return f(*args, **kwargs)

        return decorated_function

    return decorator
