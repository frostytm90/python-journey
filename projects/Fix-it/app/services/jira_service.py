from jira import JIRA
from flask import current_app
from datetime import datetime

class JiraService:
    def __init__(self):
        self.jira = None
        self.initialize_client()
    
    def initialize_client(self):
        """Initialize JIRA client with credentials from config"""
        try:
            self.jira = JIRA(
                server=current_app.config['JIRA_URL'],
                basic_auth=(
                    current_app.config['JIRA_USERNAME'],
                    current_app.config['JIRA_API_TOKEN']
                )
            )
        except Exception as e:
            current_app.logger.error(f"Failed to initialize JIRA client: {str(e)}")
            raise
    
    def get_bugs_for_project(self, project_key, start_date=None, end_date=None):
        """Fetch bugs from JIRA for a specific project and date range"""
        jql = f'project = {project_key} AND issuetype = Bug'
        
        if start_date:
            jql += f' AND created >= "{start_date.strftime("%Y-%m-%d")}"'
        if end_date:
            jql += f' AND created <= "{end_date.strftime("%Y-%m-%d")}"'
            
        try:
            issues = self.jira.search_issues(jql, maxResults=1000)
            return [{
                'jira_id': issue.key,
                'title': issue.fields.summary,
                'status': issue.fields.status.name,
                'priority': issue.fields.priority.name if hasattr(issue.fields, 'priority') else None,
                'created_at': datetime.strptime(issue.fields.created[:19], '%Y-%m-%dT%H:%M:%S'),
                'resolved_at': datetime.strptime(issue.fields.resolutiondate[:19], '%Y-%m-%dT%H:%M:%S') 
                             if issue.fields.resolutiondate else None
            } for issue in issues]
        except Exception as e:
            current_app.logger.error(f"Failed to fetch JIRA issues: {str(e)}")
            raise
    
    def update_bug_status(self, jira_id, status, resolution=None):
        """Update the status of a bug in JIRA"""
        try:
            issue = self.jira.issue(jira_id)
            transitions = self.jira.transitions(issue)
            
            # Find the transition that matches the desired status
            transition_id = None
            for t in transitions:
                if t['name'].lower() == status.lower():
                    transition_id = t['id']
                    break
            
            if transition_id:
                self.jira.transition_issue(issue, transition_id, resolution=resolution)
                return True
            else:
                current_app.logger.error(f"No transition found for status: {status}")
                return False
        except Exception as e:
            current_app.logger.error(f"Failed to update JIRA issue status: {str(e)}")
            raise
    
    def create_bug(self, summary, description, project_key):
        """Create a new bug in JIRA"""
        try:
            issue_dict = {
                'project': {'key': project_key},
                'summary': summary,
                'description': description,
                'issuetype': {'name': 'Bug'}
            }
            new_issue = self.jira.create_issue(fields=issue_dict)
            return new_issue.key
        except Exception as e:
            current_app.logger.error(f"Failed to create JIRA issue: {str(e)}")
            raise
