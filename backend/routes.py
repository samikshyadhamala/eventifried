# # from flask import Blueprint, request, jsonify
# # from app import db
# # from models import User  # Make sure you import your User model

# # bp = Blueprint('api', __name__)

# # @bp.route("/api/save-user", methods=["POST"])
# # def save_user():
# #     data = request.get_json()
# #     if not data or "email" not in data:
# #         return jsonify({"error": "Missing email"}), 400

# #     existing = User.query.filter_by(email=data["email"]).first()
# #     if existing:
# #         return jsonify({"message": "User already exists"}), 200

# #     new_user = User(
# #         name=data.get("name"),
# #         email=data["email"],
# #         image=data.get("image")
# #     )
# #     db.session.add(new_user)
# #     db.session.commit()
# #     return jsonify({"message": "User created"}), 201

# from flask import Blueprint, request, jsonify
# from .models import db, User
# from .models import OAuthUser, Event, Club
# from werkzeug.security import generate_password_hash
# from datetime import datetime

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
