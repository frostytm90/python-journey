from flask import jsonify, request
from . import api
from ..services.metrics_service import MetricsService
from ..models.event import FixitEvent
from .. import db

metrics_service = MetricsService()

@api.route('/metrics/project/<project_key>', methods=['GET'])
def get_project_metrics(project_key):
    """Get current metrics for a project"""
    try:
        metrics = metrics_service.get_project_metrics(project_key)
        technical_debt = metrics_service.calculate_technical_debt(project_key)
        
        return jsonify({
            'metrics': metrics,
            'technical_debt': technical_debt
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/metrics/event/<int:event_id>', methods=['GET'])
def get_event_metrics(event_id):
    """Get metrics comparison for a fix-it event"""
    event = FixitEvent.query.get_or_404(event_id)
    
    try:
        current_metrics = metrics_service.get_project_metrics(request.args.get('project_key'))
        current_debt = metrics_service.calculate_technical_debt(request.args.get('project_key'))
        
        metrics_comparison = {
            'bug_count': {
                'before': event.initial_bug_count,
                'after': event.resolved_bug_count,
                'improvement': event.initial_bug_count - event.resolved_bug_count
            },
            'technical_debt': {
                'before': event.initial_technical_debt,
                'after': current_debt,
                'improvement': event.initial_technical_debt - current_debt
            },
            'test_coverage': {
                'before': event.initial_test_coverage,
                'after': current_metrics['test_coverage'],
                'improvement': current_metrics['test_coverage'] - event.initial_test_coverage
            }
        }
        
        return jsonify(metrics_comparison)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/metrics/code-churn/<project_key>', methods=['GET'])
def get_code_churn(project_key):
    """Get code churn metrics for a project"""
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        churn_metrics = metrics_service.get_code_churn(
            project_key,
            start_date,
            end_date
        )
        
        return jsonify(churn_metrics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
