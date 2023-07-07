from flask import current_app, flash, redirect, render_template, request, url_for, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from app import db
from app.models import User, Event, EventGroup
from app.services import bp
import datetime





@bp.route('/add-event/<int:id>', methods=['GET', 'POST'])
@login_required
def add_event(id):
    group_data = EventGroup.query.get_or_404(id)

    if request.method == 'POST':
        # Get the form data from the request
        event_name = request.form.get('eventName')
        location = request.form.get('location')
        description = request.form.get('description')
        event_link = request.form.get('eventLink')
        event_date_str = request.form.get('eventDate')
        event_date = datetime.datetime.strptime(event_date_str, '%Y-%m-%d').replace(hour=0, minute=0, second=0)


        # Process the form data as needed
        event_saved = Event(event_name=event_name, location=location,
            description=description, event_date = event_date,
            event_link=event_link, user_id=current_user.id, 
            event_group_id = group_data.id,)
        db.session.add(event_saved)
        db.session.commit()
        # Return a JSON response indicating the success of the operation
        return jsonify({'success': True, 'message': 'Event added successfully'})

    # Render the template for displaying the form
    return render_template('services/add-event.html', title='Register', group_data=group_data)
    


@bp.route('/new-event', methods=['GET', 'POST'])
@login_required
def event_group():
    # Query database for event groups
    all_group = EventGroup.query.all()
    array_colors = ['info', 'danger', 'success', 'warning', 'primary']


    if request.method == 'POST':
        group_name = request.form.get('eventType')
        description = request.form.get('description')
        event_group = EventGroup(name=group_name, description=description)

        # Save data to DB
        db.session.add(event_group)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Event group added successfully'})
        

    return render_template('services/new_event.html', title='Register', 
    all_group=all_group, array_colors=array_colors)




@bp.route('/delete-event/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
    event_group = EventGroup.query.get_or_404(event_id)

    # Delete associated events
    events = Event.query.filter_by(event_group_id=event_group.id).all()
    for event in events:
        db.session.delete(event)

    # Delete the event group
    db.session.delete(event_group)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Event group and associated events deleted successfully'})
