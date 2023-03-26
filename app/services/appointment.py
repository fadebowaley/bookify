from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Appointment, Provider, Service, User
from app.services import bp


@bp.route('/appointments')
@login_required
def appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    return render_template('appointments.html', appointments=appointments)


@bp.route('/create-app', methods=['POST'])
def create_appointment():
    data = request.get_json()
    user_id = data.get('user_id')
    provider_id = data.get('provider_id')
    service_id = data.get('service_id')
    date = data.get('date')
    time = data.get('time')

    # Check if the user and provider exist
    user = User.query.get(user_id)
    provider = Provider.query.get(provider_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404
    elif not provider:
        return jsonify({'error': 'Provider not found.'}), 404

    # Check if the appointment slot is available
    existing_appointment = Appointment.query.filter_by(
        provider_id=provider_id, date=date, time=time).first()
    if existing_appointment:
        return jsonify({'error': 'Appointment slot not available.'}), 400

    # Create the appointment
    appointment = Appointment(
        user_id=user_id, provider_id=provider_id, service_id=service_id, date=date, time=time)
    db.session.add(appointment)
    db.session.commit()

    return jsonify({'message': 'Appointment created successfully.', 'data': appointment.to_dict()}), 201


@bp.route('/get-app', methods=['GET'])
def get_appointments():
    user_id = request.args.get('user_id')
    provider_id = request.args.get('provider_id')

    if user_id:
        appointments = Appointment.query.filter_by(user_id=user_id).all()
    elif provider_id:
        appointments = Appointment.query.filter_by(
            provider_id=provider_id).all()
    else:
        return jsonify({'error': 'Please provide a user_id or provider_id parameter.'}), 400

    appointments_data = [appointment.to_dict() for appointment in appointments]
    return jsonify({'data': appointments_data}), 200


@bp.route('/<int:id>', methods=['PUT'])
def update_appointment(id):
    appointment = Appointment.query.get(id)

    if not appointment:
        return jsonify({'error': 'Appointment not found.'}), 404

    data = request.get_json()
    appointment.user_id = data.get('user_id', appointment.user_id)
    appointment.provider_id = data.get('provider_id', appointment.provider_id)
    appointment.service_id = data.get('service_id', appointment.service_id)
    appointment.date = data.get('date', appointment.date)
    appointment.time = data.get('time', appointment.time)

    db.session.commit()

    return jsonify({'message': 'Appointment updated successfully.', 'data': appointment.to_dict()}), 200


@bp.route('/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    appointment = Appointment.query.get(id)

    if not appointment:
        return jsonify({'error': 'Appointment not found.'}), 404

    db.session.delete(appointment)
    db.session.commit()

    return jsonify({'message': 'Appointment deleted successfully.'}), 200
