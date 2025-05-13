# from . import db
# from datetime import datetime

# class OAuthUser(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     provider = db.Column(db.String(50), nullable=False)  # e.g., 'google'
#     provider_id = db.Column(db.String(120), nullable=False)  # Google ID
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image = db.Column(db.String(250))  # optional profile picture

#     def __repr__(self):
#         return f'<OAuthUser {self.email} from {self.provider}>'


# class Club(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     location = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     events = db.relationship('Event', backref='club', lazy=True)

#     def _repr_(self):
#         return f'<Club {self.name}>'

# class Event(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     event_name = db.Column(db.String(200), nullable=False)
#     date = db.Column(db.DateTime, default=datetime.now, nullable=False)
#     location = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     image_file = db.Column(db.String(30), nullable=False)
#     club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)

#     def _repr_(self):
#         return f'<{self.event_name}, {self.location}>'

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_email = db.Column(db.String(120), unique=True, nullable=False)
#     full_name = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)

#     def _repr_(self):
#         return f'<User {self.full_name}>'