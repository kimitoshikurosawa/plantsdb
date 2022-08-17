# Flask-RESTful API project

This project shows one of the possible ways to implement RESTful API server.

There are implemented two models: User and Todo, one user has many todos.

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-RESTful - restful API library.
3. Flask-Script - provides support for writing external scripts.
4. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```
.
├── README.md
├── app.py
├── endpoints
│   ├── __init__.py
│   ├── todos
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── resource.py
│   └── users
│       ├── __init__.py
│       ├── model.py
│       └── resource.py
├── manage.py
├── requirements.txt
└── settings.py
```

* endpoints - holds all endpoints.
* app.py - flask application initialization.
* settings.py - all global app settings.
* manage.py - script for managing application (migrations, server execution, etc.)

## Running 

1. Clone repository.
2. pip install requirements.txt
3. Run following commands:
    1. python manage.py db init
    2. python manage.py db migrate
    3. python manage.py db upgrade
4. Start server by running python manage.py runserver