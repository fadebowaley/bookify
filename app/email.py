import os
from threading import Thread
from flask_mail import Message
from . import mail
from app import models
from app.models import User
from flask import current_app


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
        
        
# sending emails to multiple users at the same time
def send_multiple_emails():
    # with mail.connect() as conn:
    users  = User.query.all()
    for user in users:
            # message = "text messages"
        subject = "hello, %s" % user.name
        print(subject)
    return print('All mails successfully sent')
        #     msg = Message(recipients=[user.email],
        #                   body = message,
        #                   subject = subject)  
        #     Thread(target=send_async_email,
        #    args=(current_app._get_current_object(), msg)).start()          


# os.path.join(current_app.root_path,'static/img/email/images/Logo.png')
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # with open("/brvcase/app/static/img/email/images/Logo.png") as fp:  
    #     msg.attach("Logo.png","image/png",fp.read())
    # msg.attach('Logo.png','image/png',open(os.path.join(current_app.root_path,'static/img/email/images/Logo.png'), 'rb').read(), 'inline', headers=[['Content-ID','<brvlogo>'],])    
    # msg.attach('bee.png','image/png',open(os.path.join(current_app.root_path,'static/img/email/images/bee.png'), 'rb').read(), 'inline', headers=[['Content-ID','<bee>'],])     
    # with open(os.path.join(current_app.root_path,'static/img/email/images/reminder-hero-graph.png'), 'rb') as fp:        
    #     msg.attach('reminder-hero-graph.png', 'image/png', fp.read(), 'inline', headers=[['Content-ID','<ribbon>'],])
    
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()
   

def send_notification_report(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()

def send_bday(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()

def send_anny(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()

def send_mkt(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()


