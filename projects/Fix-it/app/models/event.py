from datetime import datetime
from .. import db

class FixitEvent(db.Model):
    __tablename__ = 'fixit_events'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='planned')  # planned, active, completed
    
    # Pre-event metrics
    initial_bug_count = db.Column(db.Integer)
    initial_technical_debt = db.Column(db.Float)
    initial_test_coverage = db.Column(db.Float)
    
    # Post-event metrics
    resolved_bug_count = db.Column(db.Integer)
    final_technical_debt = db.Column(db.Float)
    final_test_coverage = db.Column(db.Float)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<FixitEvent {self.name}>'
        
class Bug(db.Model):
    __tablename__ = 'bugs'
    
    id = db.Column(db.Integer, primary_key=True)
    jira_id = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    priority = db.Column(db.String(20))
    event_id = db.Column(db.Integer, db.ForeignKey('fixit_events.id'))
    resolved_at = db.Column(db.DateTime)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    event = db.relationship('FixitEvent', backref=db.backref('bugs', lazy=True))
    
    def __repr__(self):
        return f'<Bug {self.jira_id}>'
