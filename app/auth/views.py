from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app import db
from app.forms import LoginForm, RegisterForm
from app.models import User
from app.auth import bp



@bp.route('/login', methods=['GET', 'POST'])
def login():
    """ Function that let user Login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('main.dashboard'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('auth/login.html', title='Log In', form=form)



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))




@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)



@bp.route('/password-change', methods=['GET', 'POST'])
@login_required
def security():
    if request.method == "POST":
        if current_user.is_authenticated:
            # check old password
            user = User.query.filter(User.id == current_user.id).first()
            if user.verify_password(request.form.get('current_password')):
                current_user.set_password(request.form.get('new_password'))
                db.session.commit()
                flash('password succesfully changed!, to effected on the next login')
            else:
                flash('your current password is incorrect')
    return render_template('auth/change_password.html', user=current_user,
                           title="Change Password")
