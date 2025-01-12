from flask import jsonify, request
from . import api
from ..models.event import FixitEvent
from .. import db

@api.route('/events', methods=['GET'])
def get_events():
    events = FixitEvent.query.all()
    return jsonify([{
        'id': event.id,
        'name': event.name,
        'start_date': event.start_date.isoformat(),
        'end_date': event.end_date.isoformat(),
        'status': event.status,
        'initial_bug_count': event.initial_bug_count,
        'resolved_bug_count': event.resolved_bug_count
    } for event in events])

@api.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = FixitEvent(
        name=data['name'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        status='planned'
    )
    db.session.add(event)
    db.session.commit()
    return jsonify({
        'id': event.id,
        'name': event.name,
        'status': event.status
    }), 201

@api.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = FixitEvent.query.get_or_404(event_id)
    return jsonify({
        'id': event.id,
        'name': event.name,
        'start_date': event.start_date.isoformat(),
        'end_date': event.end_date.isoformat(),
        'status': event.status,
        'initial_bug_count': event.initial_bug_count,
        'initial_technical_debt': event.initial_technical_debt,
        'initial_test_coverage': event.initial_test_coverage,
        'resolved_bug_count': event.resolved_bug_count,
        'final_technical_debt': event.final_technical_debt,
        'final_test_coverage': event.final_test_coverage
    })
