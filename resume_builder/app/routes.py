from flask import render_template, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm  # Import your forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Create an instance of your login form
    return render_template('login.html', form=form)  # Pass the form object to the template

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # Create an instance of your registration form
    return render_template('register.html', form=form)  # Pass the form object to the template

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/builder')
def resume_builder():
    return render_template('builder.html')

@app.route('/analyzer')
def resume_analyzer():
    return render_template('analyzer.html')
