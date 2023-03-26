from flask import render_template
from app.models import Location
from app.main import bp


@bp.route('/')
def homepage(): 
    print('This is the Templates show...')       
    return render_template('index.html')


# @bp.route('/')
# @cache.cached(timeout=10)
# def homepage():

#     return render_template('home/home.html')
