from app.forms import ProviderForm, ServiceForm, LocationForm
from app.models import Provider, Service, Location
from flask import Blueprint, jsonify, request
from flask import render_template, request
from app.models import Provider, Location
from app.views import bp


@bp.route('/providers')
def providers():
    location_id = request.args.get('location_id')
    if location_id:
        providers = Provider.query.filter_by(location_id=location_id).all()
        location = Location.query.get(location_id)
    else:
        providers = Provider.query.all()
        location = None
    return render_template('providers.html', providers=providers, location=location)


bp = Blueprint('providers', __name__, url_prefix='/api/providers')


@bp.route('', methods=['GET'])
def get_providers():
    """
    Returns a list of providers.
    """
    providers = Provider.query.all()
    return jsonify([provider.to_dict() for provider in providers])


@bp.route('/<int:provider_id>', methods=['GET'])
def get_provider(provider_id):
    """
    Returns a provider by ID.
    """
    provider = Provider.query.get_or_404(provider_id)
    return jsonify(provider.to_dict())


@bp.route('', methods=['POST'])
def create_provider():
    """
    Creates a new provider.
    """
    form = ProviderForm()
    if form.validate_on_submit():
        provider = Provider()
        form.populate_obj(provider)
        provider.save()
        return jsonify(provider.to_dict()), 201
    return jsonify(errors=form.errors), 400


@bp.route('/<int:provider_id>', methods=['PUT'])
def update_provider(provider_id):
    """
    Updates a provider by ID.
    """
    provider = Provider.query.get_or_404(provider_id)
    form = ProviderForm(obj=provider)
    if form.validate_on_submit():
        form.populate_obj(provider)
        provider.save()
        return jsonify(provider.to_dict())
    return jsonify(errors=form.errors), 400


@bp.route('/<int:provider_id>', methods=['DELETE'])
def delete_provider(provider_id):
    """
    Deletes a provider by ID.
    """
    provider = Provider.query.get_or_404(provider_id)
    provider.delete()
    return '', 204


@bp.route('/<int:provider_id>/services', methods=['GET'])
def get_provider_services(provider_id):
    """
    Returns a list of services provided by a provider.
    """
    services = Service.query.filter_by(provider_id=provider_id).all()
    return jsonify([service.to_dict() for service in services])


@bp.route('/<int:provider_id>/services', methods=['POST'])
def create_provider_service(provider_id):
    """
    Creates a new service for a provider.
    """
    provider = Provider.query.get_or_404(provider_id)
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(provider=provider)
        form.populate_obj(service)
        service.save()
        return jsonify(service.to_dict()), 201
    return jsonify(errors=form.errors), 400


@bp.route('/<int:provider_id>/services/<int:service_id>', methods=['PUT'])
def update_provider_service(provider_id, service_id):
    """
    Updates a service provided by a provider.
    """
    service = Service.query.get_or_404(service_id)
    form = ServiceForm(obj=service)
    if form.validate_on_submit():
        form.populate_obj(service)
        service.save()
        return jsonify(service.to_dict())
    return jsonify(errors=form.errors), 400


@bp.route('/<int:provider_id>/services/<int:service_id>', methods=['DELETE'])
def delete_provider_service(provider_id, service_id):
    """
    Deletes a service provided by a provider.
    """
    service = Service.query.get_or_404(service_id)
    service.delete()
    return '', 204


@bp.route('/<int:provider_id>/locations', methods=['GET'])
def get_provider_locations(provider_id):
    """
    Returns a list of locations where a provider provides services.
    """
    provider = Provider.query.get_or_404(provider_id)
    locations = provider.locations
    return jsonify([location.to_dict() for location in locations])
