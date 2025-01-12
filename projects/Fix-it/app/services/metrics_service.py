import requests
from flask import current_app
from datetime import datetime

class MetricsService:
    def __init__(self):
        self.sonar_url = None
        self.sonar_token = None
        self.initialize_config()
    
    def initialize_config(self):
        """Initialize SonarQube configuration"""
        self.sonar_url = current_app.config['SONARQUBE_URL']
        self.sonar_token = current_app.config['SONARQUBE_TOKEN']
    
    def get_project_metrics(self, project_key):
        """Fetch code quality metrics from SonarQube"""
        try:
            headers = {'Authorization': f'Bearer {self.sonar_token}'}
            metrics = 'bugs,vulnerabilities,code_smells,coverage,duplicated_lines_density'
            
            response = requests.get(
                f'{self.sonar_url}/api/measures/component',
                params={
                    'component': project_key,
                    'metricKeys': metrics
                },
                headers=headers
            )
            response.raise_for_status()
            
            data = response.json()
            return self._parse_metrics(data['component']['measures'])
        except Exception as e:
            current_app.logger.error(f"Failed to fetch SonarQube metrics: {str(e)}")
            raise
    
    def _parse_metrics(self, measures):
        """Parse SonarQube metrics into a structured format"""
        metrics = {}
        for measure in measures:
            metrics[measure['metric']] = float(measure['value'])
        
        return {
            'bug_density': metrics.get('bugs', 0),
            'vulnerabilities': metrics.get('vulnerabilities', 0),
            'code_smells': metrics.get('code_smells', 0),
            'test_coverage': metrics.get('coverage', 0),
            'duplicated_lines': metrics.get('duplicated_lines_density', 0)
        }
    
    def calculate_technical_debt(self, project_key):
        """Calculate technical debt score based on various metrics"""
        try:
            metrics = self.get_project_metrics(project_key)
            
            # Simple technical debt calculation formula
            # You can adjust the weights based on your priorities
            debt_score = (
                metrics['bug_density'] * 1.0 +
                metrics['vulnerabilities'] * 0.8 +
                metrics['code_smells'] * 0.5 +
                (100 - metrics['test_coverage']) * 0.3 +
                metrics['duplicated_lines'] * 0.2
            )
            
            return debt_score
        except Exception as e:
            current_app.logger.error(f"Failed to calculate technical debt: {str(e)}")
            raise
    
    def get_code_churn(self, project_key, start_date, end_date):
        """Get code churn metrics from SonarQube"""
        try:
            headers = {'Authorization': f'Bearer {self.sonar_token}'}
            
            response = requests.get(
                f'{self.sonar_url}/api/measures/search_history',
                params={
                    'component': project_key,
                    'metrics': 'ncloc,new_lines,deleted_lines',
                    'from': start_date.strftime('%Y-%m-%d'),
                    'to': end_date.strftime('%Y-%m-%d')
                },
                headers=headers
            )
            response.raise_for_status()
            
            data = response.json()
            return self._calculate_code_churn(data['measures'])
        except Exception as e:
            current_app.logger.error(f"Failed to fetch code churn metrics: {str(e)}")
            raise
    
    def _calculate_code_churn(self, measures):
        """Calculate code churn from SonarQube measures"""
        total_lines = 0
        new_lines = 0
        deleted_lines = 0
        
        for measure in measures:
            if measure['metric'] == 'ncloc':
                total_lines = float(measure['history'][-1]['value'])
            elif measure['metric'] == 'new_lines':
                new_lines = sum(float(h['value']) for h in measure['history'])
            elif measure['metric'] == 'deleted_lines':
                deleted_lines = sum(float(h['value']) for h in measure['history'])
        
        return {
            'total_lines': total_lines,
            'new_lines': new_lines,
            'deleted_lines': deleted_lines,
            'churn_rate': (new_lines + deleted_lines) / total_lines if total_lines > 0 else 0
        }
