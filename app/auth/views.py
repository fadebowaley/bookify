from flask import current_app, flash, redirect, render_template, request, url_for, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from app import db
from app.models import User
from app.auth import bp
from ..email import send_email
from .forms import LoginForm, ResetPasswordRequestForm, ResetPasswordForm, \
    RegistrationForm



@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
         return redirect(url_for('main.homepage'))

    form = RegistrationForm()

    if form.validate_on_submit:
        if request.method == 'POST':
            first_name = request.form['fullname']
            last_name = request.form['lastname']
            email = request.form['email']
            password = request.form['password']
          
            # Generate the username from the first_name and last_name
            username = f"{first_name}_{last_name}"

            # Create a new user object
            user = User(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                username=username )

            user.set_password(password)

            # Add the user to the database
            db.session.add(user)
            db.session.commit()

            # Perform login for the registered user
            login_user(user)

            flash('Registration successful!')
            return redirect(url_for('main.homepage'))

    return render_template('auth/register.html', title='Register', form=form)





@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
         return redirect(url_for('main.homepage'))

    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Check if the username and password are valid
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            # Perform login
            login_user(user)
            flash('User successfully logged in!')
            return redirect(url_for('main.homepage'))
        else:
            flash('Invalid email or password.')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html', title='Log In', form=form)


    if current_user.is_authenticated:
         return redirect(url_for('main.homepage'))

    form = LoginForm()
    if form.validate_on_submit:

        if request.method == 'POST':
            email = request.form['email']
            password= request.form['password']

            # Check if the username and password are valid
            user = User.query.filter_by(email=email).first()

            # Perform login
            if email == user.email and user.check_password(password):

                login_user(user)
                flash('User successfully login ...')
                return redirect(url_for('main.homepage'))
            else:

                flash('User successfully login ...')
                return redirect(url_for('auth.login'))

    return render_template('auth/login.html', title='Log In', form=form)




@bp.route('/logout')
@login_required
def logout():
    logout_user()

    flash('successfully logout!')
    return redirect(url_for('main.homepage'))









@bp.route('/lock', methods=['GET', 'POST'])
def lock():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
   
    return render_template('auth/lock.html', title='Register')



@bp.route('/change', methods=['GET', 'POST'])
def change():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
   
    return render_template('auth/change.html', title='Register')






@bp.route('/recover', methods=['GET', 'POST'])
def reset_password_request():
    # if current_user.is_authenticated:                                                                       
    #     return redirect(url_for('home.admin_dashboard'))

    # form = ResetPasswordRequestForm()
    # if request.method =="POST":
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user:
    #         send_reset_email(user)
    #         flash('Check your email for reset link')
    #         return redirect(url_for('auth.login'))
    #     else:
    #         flash('Check your registered email for activation links')
    return render_template('auth/request.html',
                           title='Reset Password', )




@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # if current_user.is_authenticated:                                                        
    #     return redirect(url_for('home.admin_dashboard'))
    # user = User.verify_reset_token(token)
    # if not user:
    #     flash('invalid or expired token', 'warning')
    #     return redirect(url_for('auth.login'))  
    # form = ResetPasswordForm()
    # if request.method =="POST":
    # # if form.validate_on_submit():
    #     user.set_password(form.password.data)
    #     db.session.commit()
    #     flash('Your password has been reset.')
    #     return redirect(url_for('auth.login'))
    return render_template('auth/password_reset.html',  title= "Reset password")


# After registration this link will help user to reset their password 
@bp.route('/set_password/<token>', methods=['GET', 'POST'])
def set_password(token):
    if current_user.is_authenticated:                                                               
        return redirect(url_for('home.admin_dashboard')) 

    user = User.verify_reset_token(token)
    if not user:
        flash('invalid or expired token', 'warning')
        return redirect(url_for('auth.login'))  
    form = ResetPasswordForm()
    if request.method =="POST":
    # if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Password Updated! Welcome!!.')        
        login_user(user)
        email = user.email
        session['email'] = email
        value = session.get('email')
                                                                    
        return redirect(url_for('home.admin_dashboard'))

     
    return render_template('auth/set_password2.html', form=form, title= "Start with a password")



