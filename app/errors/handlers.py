from flask import render_template
from app import db
from app.errors import bp
from flask_wtf.csrf import CSRFError


@bp.app_errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(413)
def payload_too_large(error):
    db.session.rollback()
    return render_template('errors/413.html'), 413


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500


@bp.app_errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('errors/csrf_error.html', reason=e.description), 400
