from flask import render_template
from app.models import Location
from app.views import bp


@bp.route('/locations')
def locations():
    locations = Location.query.all()
    return render_template('locations.html', locations=locations)
