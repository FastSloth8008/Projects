from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resume_builder.db'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'  # Set the login view for redirect
login_manager.init_app(app)

# Define user loader function for Flask-Login
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes and models
from app import routes, models
