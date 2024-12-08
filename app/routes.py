from flask import Blueprint, render_template, send_from_directory

# Define the blueprint
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return render_template('home.html')

@main_routes.route('/about')
def about():
    return render_template('about.html')

@main_routes.route('/skills')
def skills():
    return render_template('skills.html')

@main_routes.route('/experience')
def experience():
    return render_template('experience.html')

@main_routes.route('/education')
def education():
    return render_template('education.html')

@main_routes.route('/projects')
def projects():
    return render_template('projects.html')

@main_routes.route('/contact')
def contact():
    return render_template('contact.html')

@main_routes.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')