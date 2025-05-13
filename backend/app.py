# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from datetime import datetime
# from werkzeug.security import generate_password_hash
# import logging
# from datetime import datetime
# from flask import Blueprint, request, jsonify

# # app = Flask(__name__)
# # CORS(app)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventify.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # db = SQLAlchemy(app)
# # migrate = Migrate(app, db)

# logging.basicConfig(level=logging.INFO)

# #added
# def create_app():
#     app = Flask(__name__)
#     CORS(app)

#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventify.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.init_app(app)
#     migrate.init_app(app, db)

#     # Import models so they are registered
#     from . import models
#     from .routes import bp as api_bp
#     app.register_blueprint(api_bp)

#     return app

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
#  #added
    
# bp = Blueprint('api', __name__)

# @bp.route("/api/save-user", methods=["POST"])
# def save_user():
#     data = request.get_json()
#     if not data or "email" not in data:
#         return jsonify({"error": "Missing email"}), 400

#     existing = User.query.filter_by(email=data["email"]).first()
#     if existing:
#         return jsonify({"message": "User already exists"}), 200

#     new_user = User(
#         name=data.get("name"),
#         email=data["email"],
#         image=data.get("image")
#     )
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": "User created"}), 201


# @app.route('/api/club_signup', methods=['POST','GET'])
# def club_signup():
#     try:
#         data = request.get_json(force=True)
#         app.logger.info(f"Received signup data: {data}")

#         name = data.get('name', '').strip()
#         email = data.get('email', '').strip().lower()
#         location = data.get('location', '').strip()
#         password = data.get('password')

#         if not all([name, email, location, password]):
#             return jsonify({'error': 'All fields are required'}), 400

#         if Club.query.filter_by(email=email).first():
#             return jsonify({'error': 'Email already registered'}), 409

#         hashed_password = generate_password_hash(password)

#         new_club = Club(name=name, email=email, location=location, password=hashed_password)
#         db.session.add(new_club)
#         db.session.commit()

#         return jsonify({'message': 'Club registered successfully!'}), 201

#     except Exception as e:
#         import traceback
#         app.logger.error(f"Exception occurred: {e}")
#         traceback.print_exc()
#         return jsonify({'error': 'Internal server error'}), 500
    
# # @app.route('/api/create_event', methods=['POST'])
# # def create_event():
# #     try:
# #         data = request.get_json(force=True)
# #         app.logger.info(f"Received event data: {data}")

# #         event_name = data.get('event_name', '').strip()
# #         date = datetime.strptime(data.get('date'), '%Y-%m-%d')  # or '%Y-%m-%d %H:%M' if time is included
# #         location = data.get('location', '').strip()
# #         description = data.get('description', '')
# #         image_file = data.get('image_file', 'default.jpg')  # optional: store filename/path
# #         club_id = data.get('club_id')

# #         if not all([event_name, date, location, club_id]):
# #             return jsonify({'error': 'Missing required fields'}), 400

# #         event = Event(
# #             event_name=event_name,
# #             date=date,
# #             locatio=location,
# #             description=description,
# #             image_file=image_file,
# #             club_id=club_id
# #         )

# #         db.session.add(event)
# #         db.session.commit()

# #         return jsonify({'message': 'Event created successfully!'}), 201

# #     except Exception as e:
# #         app.logger.error(f"Exception: {e}")
# #         return jsonify({'error': 'Internal server error'}), 500

# @app.route('/api/create_event', methods=['POST'])
# def create_event():
#     try:
#         data = request.get_json(force=True)
#         app.logger.info(f"Received event data: {data}")

#         event_name = data.get('event_name', '').strip()
#         date = datetime.strptime(data.get('date'), '%Y-%m-%d')
#         location = data.get('location', '').strip()
#         description = data.get('description', '')
#         image_file = data.get('image_file', 'default.jpg')
#         club_id = data.get('club_id')

#         if not all([event_name, date, location, club_id]):
#             return jsonify({'error': 'Missing required fields'}), 400

#         event = Event(
#             event_name=event_name,
#             date=date,
#             location=location,
#             description=description,
#             image_file=image_file,
#             club_id=club_id
#         )

#         db.session.add(event)
#         db.session.commit()

#         return jsonify({'message': 'Event created successfully!'}), 201

#     except Exception as e:
#         app.logger.error(f"Exception: {e}")
#         return jsonify({'error': 'Internal server error'}), 500

# @app.route('/api/events', methods=['GET'])
# def get_events():
#     events = Event.query.all()
#     events_list = []

#     for event in events:
#         events_list.append({
#             'id': event.id,
#             'event_name': event.event_name,
#             'date': event.date.strftime('%Y-%m-%d'),
#             'location': event.location,
#             'description': event.description,
#             'image_file': event.image_file,
#             'club_name': event.club.name  # via backref
#         })

#     return jsonify(events_list), 200


# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
       
#     print("Running app...")

#     app.run(debug=True)

# from flask import Flask, request, jsonify, Blueprint
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from werkzeug.security import generate_password_hash
# from datetime import datetime
# import logging

# # Global db and migrate objects
# db = SQLAlchemy()
# migrate = Migrate()

# # Blueprint for all routes
# bp = Blueprint('api', __name__)

# # Logging setup
# logging.basicConfig(level=logging.INFO)

# # Models
# class OAuthUser(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     provider = db.Column(db.String(50), nullable=False)
#     provider_id = db.Column(db.String(120), nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image = db.Column(db.String(250))

#     def __repr__(self):
#         return f'<OAuthUser {self.email} from {self.provider}>'

# class Club(db.Model):
#     is_google_account = db.Column(db.Boolean, default=False)
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
#     password = db.Column(db.String(120), nullable=True)  # Optional for Google
#     is_google_account = db.Column(db.Boolean, default=False)  # Flag to indicate Google sign-up
    
#     def __repr__(self):
#         return f'<User {self.full_name}>'
# # Routes using blueprint
# @bp.route("/api/save-user", methods=["POST"])
# def save_user():
#     data = request.get_json()
#     if not data or "email" not in data:
#         return jsonify({"error": "Missing email"}), 400

#     existing = OAuthUser.query.filter_by(email=data["email"]).first()
#     if existing:
#         return jsonify({"message": "User already exists"}), 200

#     new_user = OAuthUser(
#         name=data.get("name"),
#         email=data["email"],
#         image=data.get("image"),
#         provider="google",  # example static value
#         provider_id=data.get("provider_id", "")
#     )
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": "User created"}), 201

# @bp.route('/api/user_signup', methods=['POST'])
# def user_signup():
#     data = request.get_json(force=True)
#     full_name = data.get('full_name', '').strip()
#     email = data.get('email', '').strip().lower()
#     password = data.get('password')  # Optional for Google
#     is_google = data.get('is_google_account', False)

#     if not all([full_name, email]):
#         return jsonify({'error': 'Full name and email are required'}), 400

#     # Check if the user already exists in OAuthUser
#     existing_oauth_user = OAuthUser.query.filter_by(email=email).first()
#     if existing_oauth_user:
#         # Save the data in the User table as well
#         existing_user = User.query.filter_by(user_email=email).first()
#         if not existing_user:
#             new_user = User(
#                 user_email=email,
#                 full_name=full_name,
#                 is_google_account=True  # Google account flag
#             )
#             db.session.add(new_user)
#             db.session.commit()
#         return jsonify({'message': 'User already exists'}), 200

#     # If it's a Google sign-up, no password is required
#     if is_google:
#         new_oauth_user = OAuthUser(
#             name=full_name,
#             email=email,
#             provider="google",  # Static value
#             provider_id=data.get("provider_id", ""),
#             image=data.get("image", "")
#         )
#         db.session.add(new_oauth_user)
#         db.session.commit()

#         new_user = User(
#             user_email=email,
#             full_name=full_name,
#             is_google_account=True  # Google account flag
#         )
#         db.session.add(new_user)
#         db.session.commit()

#         return jsonify({'message': 'User registered successfully!'}), 201

#     # Handle traditional signup with password
#     if not password:
#         return jsonify({'error': 'Password is required for manual sign-up'}), 400
#     hashed_password = generate_password_hash(password)
#     new_user = User(
#         user_email=email,
#         full_name=full_name,
#         password=hashed_password,
#         is_google_account=False  # Manual account flag
#     )

#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'message': 'User registered successfully!'}), 201


# @bp.route('/api/club_signup', methods=['POST'])
# def club_signup():
#     data = request.get_json(force=True)
#     name = data.get('name', '').strip()
#     email = data.get('email', '').strip().lower()
#     location = data.get('location', '').strip()
#     password = data.get('password')  # Optional for Google
#     is_google = data.get('is_google_account', False)

#     if not all([name, email, location]):
#         return jsonify({'error': 'Missing required fields'}), 400

#     # Check if the club already exists in OAuthUser
#     existing_oauth_user = OAuthUser.query.filter_by(email=email).first()
#     if existing_oauth_user:
#         # Save the data in the Club table as well
#         existing_club = Club.query.filter_by(email=email).first()
#         if not existing_club:
#             new_club = Club(
#                 name=name,
#                 email=email,
#                 location=location,
#                 is_google_account=True  # Google account flag
#             )
#             db.session.add(new_club)
#             db.session.commit()
#         return jsonify({'message': 'Club already exists'}), 200

#     # If it's a Google sign-up, no password is required
#     if is_google:
#         new_oauth_user = OAuthUser(
#             name=name,
#             email=email,
#             provider="google",  # Static value
#             provider_id=data.get("provider_id", ""),
#             image=data.get("image", "")
#         )
#         db.session.add(new_oauth_user)
#         db.session.commit()

#         new_club = Club(
#             name=name,
#             email=email,
#             location=location,
#             is_google_account=True  # Google account flag
#         )
#         db.session.add(new_club)
#         db.session.commit()

#         return jsonify({'message': 'Club registered successfully!'}), 201

#     # Handle traditional signup with password
#     if not password:
#         return jsonify({'error': 'Password is required for manual sign-up'}), 400
#     hashed_password = generate_password_hash(password)
#     new_club = Club(
#         name=name,
#         email=email,
#         location=location,
#         password=hashed_password,
#         is_google_account=False  # Manual account flag
#     )

#     db.session.add(new_club)
#     db.session.commit()

#     return jsonify({'message': 'Club registered successfully!'}), 201

# # @bp.route('/api/club_signup', methods=['POST'])
# # def club_signup():
# #     data = request.get_json(force=True)
# #     name = data.get('name', '').strip()
# #     email = data.get('email', '').strip().lower()
# #     location = data.get('location', '').strip()
# #     password = data.get('password')

# #     if not all([name, email, location, password]):
# #         return jsonify({'error': 'All fields are required'}), 400

# #     if Club.query.filter_by(email=email).first():
# #         return jsonify({'error': 'Email already registered'}), 409

# #     hashed_password = generate_password_hash(password)
# #     new_club = Club(name=name, email=email, location=location, password=hashed_password)
# #     db.session.add(new_club)
# #     db.session.commit()

# #     return jsonify({'message': 'Club registered successfully!'}), 201
# # @bp.route('/api/club_signup', methods=['POST'])
# # def club_signup():
# #     data = request.get_json(force=True)
# #     name = data.get('name', '').strip()
# #     email = data.get('email', '').strip().lower()
# #     location = data.get('location', '').strip()
# #     password = data.get('password')  # Optional for Google
# #     is_google = data.get('is_google_account', False)

# #     if not all([name, email, location]):
# #         return jsonify({'error': 'Missing required fields'}), 400

# #     # Check if the club already exists
# #     existing_club = Club.query.filter_by(email=email).first()
# #     if existing_club:
# #         return jsonify({'error': 'Club already exists'}), 409

# #     # If it's a Google sign-up, no password is required
# #     if is_google:
# #         new_club = Club(
# #             name=name,
# #             email=email,
# #             location=location,
# #             is_google_account=True  # Google account flag
# #         )
# #     else:
# #         if not password:
# #             return jsonify({'error': 'Password is required for manual sign-up'}), 400
# #         hashed_password = generate_password_hash(password)
# #         new_club = Club(
# #             name=name,
# #             email=email,
# #             location=location,
# #             password=hashed_password,
# #             is_google_account=False  # Manual account flag
# #         )

# #     db.session.add(new_club)
# #     db.session.commit()

# #     return jsonify({'message': 'Club registered successfully!'}), 201



# @bp.route('/api/create_event', methods=['POST'])
# def create_event():
#     data = request.get_json(force=True)
#     event_name = data.get('event_name', '').strip()
#     date = datetime.strptime(data.get('date'), '%Y-%m-%d')
#     location = data.get('location', '').strip()
#     description = data.get('description', '')
#     image_file = data.get('image_file', 'default.jpg')
#     club_id = data.get('club_id')

#     if not all([event_name, date, location, club_id]):
#         return jsonify({'error': 'Missing required fields'}), 400

#     event = Event(
#         event_name=event_name,
#         date=date,
#         location=location,
#         description=description,
#         image_file=image_file,
#         club_id=club_id
#     )

#     db.session.add(event)
#     db.session.commit()
#     return jsonify({'message': 'Event created successfully!'}), 201

# @bp.route('/api/events', methods=['GET'])
# def get_events():
#     events = Event.query.all()
#     events_list = []
#     for event in events:
#         events_list.append({
#             'id': event.id,
#             'event_name': event.event_name,
#             'date': event.date.strftime('%Y-%m-%d'),
#             'location': event.location,
#             'description': event.description,
#             'image_file': event.image_file,
#             'club_name': event.club.name
#         })
#     return jsonify(events_list), 200

# # @bp.route('/api/club_login', methods=['POST'])
# # def club_login():
# #     data = request.get_json()
# #     email = data.get('email', '').strip().lower()
# #     password = data.get('password', '')
# #     is_google = data.get('is_google_account', False)

# #     club = Club.query.filter_by(email=email).first()
# #     if not club:
# #         return jsonify({'error': 'Club not found'}), 404

# #     if is_google:
# #         if club.is_google_account:
# #             return jsonify({'message': 'Login successful (Google)', 'club_id': club.id}), 200
# #         else:
# #             return jsonify({'error': 'Account not registered via Google'}), 403

# #     # Traditional login
# #     if not password:
# #         return jsonify({'error': 'Password required'}), 400

# #     from werkzeug.security import check_password_hash
# #     if check_password_hash(club.password, password):
# #         return jsonify({'message': 'Login successful', 'club_id': club.id}), 200
# #     else:
# #         return jsonify({'error': 'Invalid password'}), 401

# # @bp.route('/api/user_signup', methods=['POST'])
# # def user_signup():
# #     data = request.get_json(force=True)
# #     full_name = data.get('full_name', '').strip()
# #     email = data.get('email', '').strip().lower()
# #     password = data.get('password')  # Optional for Google
# #     is_google = data.get('is_google_account', False)

# #     if not all([full_name, email]):
# #         return jsonify({'error': 'Full name and email are required'}), 400

# #     # Check if the user already exists
# #     existing_user = User.query.filter_by(user_email=email).first()
# #     if existing_user:
# #         return jsonify({'error': 'User already exists'}), 409

# #     # If it's a Google sign-up, no password is required
# #     if is_google:
# #         new_user = User(
# #             user_email=email,
# #             full_name=full_name,
# #             is_google_account=True  # Google account flag
# #         )
# #     else:
# #         if not password:
# #             return jsonify({'error': 'Password is required for manual sign-up'}), 400
# #         hashed_password = generate_password_hash(password)
# #         new_user = User(
# #             user_email=email,
# #             full_name=full_name,
# #             password=hashed_password,
# #             is_google_account=False  # Manual account flag
# #         )
    
# #     db.session.add(new_user)
# #     db.session.commit()

# #     return jsonify({'message': 'User registered successfully!'}), 201

# @bp.route('/api/user_login', methods=['POST'])
# def user_login():
#     data = request.get_json(force=True)
#     email = data.get('email', '').strip().lower()
#     password = data.get('password', '')
#     is_google = data.get('is_google_account', False)

#     user = User.query.filter_by(user_email=email).first()
#     if not user:
#         return jsonify({'error': 'User not found'}), 404

#     if is_google:
#         if user.is_google_account:
#             return jsonify({'message': 'Login successful (Google)', 'user_id': user.id}), 200
#         else:
#             return jsonify({'error': 'Account not registered via Google'}), 403

#     if not password:
#         return jsonify({'error': 'Password required'}), 400

#     from werkzeug.security import check_password_hash
#     if check_password_hash(user.password, password):
#         return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
#     else:
#         return jsonify({'error': 'Invalid password'}), 401

# # App Factory
# def create_app():
#     app = Flask(__name__)
#     CORS(app)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventify.db' 
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app)
#     migrate.init_app(app, db)
#     app.register_blueprint(bp)
#     return app

# # Main entry point
# if __name__ == '__main__':
#     app = create_app()
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_cors import CORS
from werkzeug.security import check_password_hash
from datetime import datetime
import logging
import os


app = Flask(__name__)
CORS(app)

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'event_db.db')


# --- Configuration ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_db.db'  # Use SQLite for testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Blueprint for all routes
bp = Blueprint('api', __name__)


# Logging setup
logging.basicConfig(level=logging.INFO)

# --- Models ---
class OAuthUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50), nullable=False)
    provider_id = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(250))

class Event(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_file = db.Column(db.String(30), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    full_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=True)  # Optional for Google
    is_google_account = db.Column(db.Boolean, default=False)


class Club(db.Model):
    is_google_account = db.Column(db.Boolean, default=False)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    events = db.relationship('Event', backref='club', lazy=True)


# --- Routes ---
@bp.route("/api/save-user", methods=["POST"])
def save_user():
    data = request.get_json()
    if not data or "email" not in data:
        return jsonify({"error": "Missing email"}), 400

    existing = OAuthUser.query.filter_by(email=data["email"]).first()
    if existing:
        return jsonify({"message": "User already exists"}), 200

    new_user = OAuthUser(
        name=data.get("name"),
        email=data["email"],
        image=data.get("image"),
        provider="google",  # example static value
        provider_id=data.get("provider_id", "")
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@app.route('/api/user_signup', methods=['POST'])
def user_signup():
    data = request.get_json(force=True)
    full_name = data.get('full_name', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password')
    is_google = data.get('is_google_account', False)
    provider_id = data.get('provider_id', '')
    image = data.get('image', '')

    if not full_name or not email:
        return jsonify({'error': 'Full name and email are required'}), 400

    if User.query.filter_by(user_email=email).first():
        return jsonify({'message': 'User already exists'}), 200

    if is_google:
        if not OAuthUser.query.filter_by(email=email).first():
            oauth_user = OAuthUser(
                name=full_name,
                email=email,
                provider='google',
                provider_id=provider_id,
                image=image
            )
            db.session.add(oauth_user)

        user = User(
            user_email=email,
            full_name=full_name,
            is_google_account=True
        )
    else:
        if not password:
            return jsonify({'error': 'Password is required for manual signup'}), 400

        hashed_password = generate_password_hash(password)
        user = User(
            user_email=email,
            full_name=full_name,
            password=hashed_password,
            is_google_account=False
        )

    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/api/club_signup', methods=['GET','POST'])
def club_signup():
    data = request.get_json(force=True)
    name = data.get('name', '').strip()
    email = data.get('email', '').strip().lower()
    location = data.get('location', '').strip()
    password = data.get('password')
    is_google = data.get('is_google_account', False)
    provider_id = data.get('provider_id', '')
    image = data.get('image', '')

    if not name or not email or not location:
        return jsonify({'error': 'Name, email, and location are required'}), 400

    if Club.query.filter_by(email=email).first():
        return jsonify({'message': 'Club already exists'}), 200

    if is_google:
        if not OAuthUser.query.filter_by(email=email).first():
            oauth_user = OAuthUser(
                name=name,
                email=email,
                provider='google',
                provider_id=provider_id,
                image=image
            )
            db.session.add(oauth_user)

        club = Club(
            name=name,
            email=email,
            location=location,
            is_google_account=True
        )
    else:
        if not password:
            return jsonify({'error': 'Password is required for manual signup'}), 400

        hashed_password = generate_password_hash(password)
        club = Club(
            name=name,
            email=email,
            location=location,
            password=hashed_password,
            is_google_account=False
        )

    db.session.add(club)
    db.session.commit()
    return jsonify({'message': 'Club registered successfully'}), 201


@app.route('/api/user_login', methods=['POST'])
def user_login():
    data = request.get_json(force=True)
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    is_google = data.get('is_google_account', False)

    user = User.query.filter_by(user_email=email).first()
    if not user:
        return jsonify({'error': 'User does not exist'}), 404

    if is_google:
        if not user.is_google_account:
            return jsonify({'error': 'User signed up manually, use password login'}), 400
        return jsonify({'message': 'Google user login successful'}), 200

    # Manual login
    if user.is_google_account:
        return jsonify({'error': 'User signed up with Google, use Google login'}), 400

    if not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid password'}), 401

    return jsonify({'message': 'Manual user login successful'}), 200


@app.route('/api/club_login', methods=['POST'])
def club_login():
    data = request.get_json(force=True)
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    is_google = data.get('is_google_account', False)

    club = Club.query.filter_by(email=email).first()
    if not club:
        return jsonify({'error': 'Club does not exist'}), 404

    if is_google:
        if not club.is_google_account:
            return jsonify({'error': 'Club signed up manually, use password login'}), 400
        return jsonify({'message': 'Google club login successful'}), 200

    # Manual login
    if club.is_google_account:
        return jsonify({'error': 'Club signed up with Google, use Google login'}), 400

    if not check_password_hash(club.password, password):
        return jsonify({'error': 'Invalid password'}), 401

    return jsonify({'message': 'Manual club login successful'}), 200


# --- Run & Create DB ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.register_blueprint(bp)
    app.run(debug=True)

