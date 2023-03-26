from flask import render_template, request
from app.models import Service, Location
from app.services import bp


@bp.route('/services')
def services():
    location_id = request.args.get('location_id')
    if location_id:
        services = Service.query.filter_by(location_id=location_id).all()
        location = Location.query.get(location_id)
    else:
        services = Service.query.all()
        location = None
    return render_template('services.html', services=services, location=location)
