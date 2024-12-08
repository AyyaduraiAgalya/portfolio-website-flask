from flask import Blueprint, render_template, request, flash

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/skills')
def skills():
    return render_template('skills.html')

@main.route('/experience')
def experience():
    return render_template('experience.html')

@main.route('/education')
def education():
    return render_template('education.html')

@main.route('/projects')
def projects():
    return render_template('projects.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')