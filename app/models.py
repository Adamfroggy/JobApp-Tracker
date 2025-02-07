from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume = db.Column(db.String(200))
    cover_letter = db.Column(db.String(500))
    photo = db.Column(db.String(200))
    summary = db.Column(db.String(500))
    contact_info = db.Column(db.String(200))


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    company = db.Column(db.String(100))
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reviews = db.relationship('Review', backref='job', lazy=True)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.String(1000))
    rating = db.Column(db.Integer)  # Rating scale: 1-5
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="Applied")
    date_applied = db.Column(db.Date, nullable=False)
