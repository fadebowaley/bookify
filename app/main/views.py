from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app.main import bp
from middleware  import send_email
from app.models import Event


@bp.route('/')
def landing(): 

    return render_template('home/landing.html')
    

@bp.route('/dashboard')
def homepage():

    all_event = Event.query.all()
        
    array_colors = ['info', 'danger', 'success', 'warning', 'primary']

    return render_template('home/home.html', all_event=all_event, array_colors=array_colors)



@bp.route('/dashboard')
def dashboard():
    # Query database for event groups
    all_event = Event.query.all()

    array_colors = ['info', 'danger', 'success', 'warning', 'primary']


    return render_template('home/home.html', all_event=all_event, array_colors=array_colors)



@bp.route('/schedule', methods=['GET', 'POST'])
def schedule():
    return render_template('services/main-my-schedule.html')



@bp.route('/privacy')
def policy():
    return render_template('home/privacy-policy.html')


@bp.route('/faqs')
def faqs(): 
    print('This is the Templates show faqs...')       
    return render_template('home/faq.html')


