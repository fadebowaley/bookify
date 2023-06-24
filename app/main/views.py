from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app.models import Location
from app.main import bp
from middleware  import send_email


@bp.route('/')
def homepage(): 
    print('This is the Templates show...')       
    return render_template('home/home.html')


@bp.route('/dashboard')
def dashboard(): 
    print('This is the Templates show...')       
    return render_template('home/home.html')



@bp.route('/schedule', methods=['GET', 'POST'])
def schedule():
    return render_template('services/main-my-schedule.html')


@bp.route('/about')
def about(): 
    print('This is the Templates show...')       
    return render_template('home/about.html')


@bp.route('/privacy')
def policy():
    return render_template('home/privacy-policy.html')


@bp.route('/use-case')
def use_case(): 
    print('This is the Templates show...')       
    return render_template('home/usecase.html')


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Do something with the form data, such as send an email or save to a database
        # For example:
        send_email(name, email, message)

        flash('Thank you for contacting us. We will get back to you shortly.', 'success')
        return redirect(url_for('home.contact'))

    # If the request method is GET, simply render the contact page
    return render_template('home/contact.html')
