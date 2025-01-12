from flask import jsonify, request
from . import api
from ..services.jira_service import JiraService
from ..models.event import Bug, FixitEvent
from .. import db
from datetime import datetime

jira_service = JiraService()

@api.route('/bugs/sync/<int:event_id>', methods=['POST'])
def sync_bugs(event_id):
    """Sync bugs from JIRA for a specific event"""
    event = FixitEvent.query.get_or_404(event_id)
    
    try:
        project_key = request.json.get('project_key')
        bugs = jira_service.get_bugs_for_project(
            project_key,
            event.start_date,
            event.end_date
        )
        
        # Update local bug database
        for bug_data in bugs:
            bug = Bug.query.filter_by(jira_id=bug_data['jira_id']).first()
            if bug is None:
                bug = Bug(
                    jira_id=bug_data['jira_id'],
                    title=bug_data['title'],
                    status=bug_data['status'],
                    priority=bug_data['priority'],
                    event_id=event_id,
                    resolved_at=bug_data['resolved_at']
                )
                db.session.add(bug)
            else:
                bug.status = bug_data['status']
                bug.resolved_at = bug_data['resolved_at']
        
        db.session.commit()
        
        # Update event metrics
        event.initial_bug_count = len(bugs)
        event.resolved_bug_count = len([b for b in bugs if b['resolved_at'] is not None])
        db.session.commit()
        
        return jsonify({
            'message': 'Bugs synced successfully',
            'total_bugs': len(bugs),
            'resolved_bugs': event.resolved_bug_count
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@api.route('/bugs/event/<int:event_id>', methods=['GET'])
def get_event_bugs(event_id):
    """Get all bugs for a specific event"""
    bugs = Bug.query.filter_by(event_id=event_id).all()
    return jsonify([{
        'id': bug.id,
        'jira_id': bug.jira_id,
        'title': bug.title,
        'status': bug.status,
        'priority': bug.priority,
        'resolved_at': bug.resolved_at.isoformat() if bug.resolved_at else None
    } for bug in bugs])

@api.route('/bugs/<string:jira_id>/status', methods=['PUT'])
def update_bug_status(jira_id):
    """Update bug status in both JIRA and local database"""
    try:
        status = request.json.get('status')
        resolution = request.json.get('resolution')
        
        # Update in JIRA
        jira_service.update_bug_status(jira_id, status, resolution)
        
        # Update local database
        bug = Bug.query.filter_by(jira_id=jira_id).first_or_404()
        bug.status = status
        if status.lower() in ['resolved', 'closed', 'done']:
            bug.resolved_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Bug status updated successfully',
            'jira_id': jira_id,
            'status': status
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
