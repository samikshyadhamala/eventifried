# from flask import jsonify, request,Flask
# from app import db
# from app.models import Event

# app=Flask(__name__)
# # Route to create a new event
# @app.route('/api/create_event', methods=['POST'])
# def create_event():
#     data = request.get_json()

#     # Validate the input data
#     title = data.get('title')
#     description = data.get('description')
#     date = data.get('date')
#     location = data.get('location')

#     if not title or not description or not date or not location:
#         return jsonify({'message': 'Missing required fields'}), 400

#     # Create a new event and store it in the database
#     new_event = Event(title=title, description=description, date=date, location=location)
#     db.session.add(new_event)
#     db.session.commit()

#     return jsonify({'message': 'Event created successfully', 'event': {'title': title, 'date': date, 'location': location}}), 201

# # Route to fetch all events
# @app.route('/api/all_events', methods=['GET'])
# def all_events():
#     events = Event.query.all()
#     events_list = []
#     for event in events:
#         events_list.append({
#             'title': event.title,
#             'description': event.description,
#             'date': event.date,
#             'location': event.location,
#         })
#     return jsonify(events_list), 200
