from werkzeug.security import check_password_hash, generate_password_hash

from app import login, db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    phone = db.Column(db.String(64))

    roles = db.relationship('Role', secondary='user_roles', passive_deletes=True)
    candidate = db.relationship('Candidate', uselist=False, backref='user', passive_deletes=True)

    def __repr__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def allowed(self, access_level):
        for role in self.roles:
            if role.id == access_level:
                return True
        return False

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))


class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    country = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref='address', uselist=False)


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))

    work_experience = db.relationship('CandidateWorkExperience', backref='candidate', lazy='dynamic', passive_deletes=True)
    education = db.relationship('CandidateEducation', backref='candidate', lazy='dynamic', passive_deletes=True)
    skills = db.relationship('CandidateSkills', backref='candidate', lazy='dynamic', passive_deletes=True)
    languages = db.relationship('CandidateLanguages', backref='candidate', lazy='dynamic', passive_deletes=True)
    job_interests = db.relationship('CandidateJobInterests', backref='candidate', lazy='dynamic', passive_deletes=True)


class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    company_name = db.Column(db.String(64))


class CandidateEducation(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id', ondelete='CASCADE'))
    degree_name = db.Column(db.String(64))
    university = db.Column(db.String(64))
    year_of_graduation = db.Column(db.DateTime)
    currently_enrolled = db.Column(db.Boolean)


class CandidateWorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id', ondelete='CASCADE'))
    company_name = db.Column(db.String(64))
    job_title = db.Column(db.String(64))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    currently_working = db.Column(db.Boolean)


class CandidateSkills(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id', ondelete='CASCADE'))
    skill_name = db.Column(db.String(64))


class CandidateLanguages(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id', ondelete='CASCADE'))
    language_name = db.Column(db.String(64))
    fluency = db.Column(db.String(64))


class CandidateJobInterests(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id', ondelete='CASCADE'))
    position_name = db.Column(db.String(64))
    company_name = db.Column(db.String(64))
    salary_upper_bound = db.Column(db.Integer)
    salary_lower_bound = db.Column(db.Integer)
