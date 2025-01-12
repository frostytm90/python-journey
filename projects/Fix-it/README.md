# Fix-it Week Tool

A comprehensive solution for tracking and enhancing code health during fix-it events.

## Features

- Bug tracking and reporting
- Code health metrics monitoring
- JIRA integration
- Real-time dashboards
- Historical analysis
- Role-based access control

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Initialize the database:
```bash
flask db upgrade
```

5. Run the application:
```bash
flask run
```

## Project Structure

```
Fix-it/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── utils/
├── tests/
├── migrations/
├── config.py
├── requirements.txt
└── README.md
```

## Development

- Run tests: `pytest`
- Generate coverage report: `coverage run -m pytest`
- View coverage report: `coverage report`

## License

MIT License
