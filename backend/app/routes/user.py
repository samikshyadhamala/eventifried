# from flask import Blueprint, jsonify
# from ..models import Event

# user_bp = Blueprint('user', __name__)

# @user_bp.route('/events', methods=['GET'])
# def get_events():
#     events = Event.query.all()
#     return jsonify([{'id': e.id, 'title': e.title, 'description': e.description, 'date': e.date} for e in events])

# @user_bp.route('/event/<int:event_id>', methods=['GET'])
# def get_event(event_id):
#     event = Event.query.get_or_404(event_id)
#     return jsonify({'title': event.title, 'description': event.description, 'date': event.date})
