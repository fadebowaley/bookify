from flask import render_template
from app.models import Location
from app.main import bp


@bp.route('/')
def main():
        
    return render_template('index.html')
