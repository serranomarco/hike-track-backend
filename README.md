# hike-track-backend

## Setup
1. Clone project
2. Create .env files in the root directory (example.env included)
3. install packages with venv
4. From the root directory, run [flask run] (in venv)

### Steps to Configure Project
1. Run the following to confirm that Flask is configured correctly:
```bash
pipenv shell  # start venv flask run
flask run     # start app on port 5000 by default
```
2. Run the following to confirm database connection to app:
```bash
flask db init   # will create migrations folder

# add to migrations/alembic.ini for time stamps on migrations:
file_template = %%(year)d%%(month).2d%%(day).2d_%%(hour).2d%%(minute).2d%%(second).2d_%%(slug)s

# after models have been created run the following commands:
flask db migrate -m 'comment'   # will create tables migration files from models
flask db upgrade                # will create tables in database
```

### Python Flask:
- JWT Auth
- Werkzeug Security for password encryption
- API Endpoints for User/Posts/Location CRUD

### Package List
- Flask
- SQLAlchemy
- Alembic
- Flask
- python-dotenv
- psycopg2-binary
- boto3

## API Endpoints

### User
- Create User
- Delete User
- Update User
- Return Users
- User Auth -> /token

### Post
- Create Post
- Delete Post
- Update Post
- Return a Post
- Return all posts a user follows
- Return posts for a user

### Location
- Create a location
- Update a location
- Delete a location
- Return a location
- Return all locations
