# from flask import Blueprint, request, jsonify
# from ..models import Event, db

# organizer_bp = Blueprint('organizer', __name__)

# @organizer_bp.route('/event', methods=['POST'])
# def create_event():
#     data = request.get_json()
#     new_event = Event(
#         title=data['title'],
#         description=data.get('description', ''),
#         date=data['date'],
#         organizer_id=data['organizer_id']
#     )
#     db.session.add(new_event)
#     db.session.commit()
#     return jsonify({'message': 'Event created'}), 201

# @organizer_bp.route('/events', methods=['GET'])
# def get_organizer_events():
#     organizer_id = request.args.get('organizer_id')
#     events = Event.query.filter_by(organizer_id=organizer_id).all()
#     return jsonify([e.title for e in events])
