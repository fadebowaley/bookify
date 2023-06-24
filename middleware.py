from flask import render_template, current_app
#from flask_babel import _
from email.utils import formataddr
from flask import *  
from flask_mail import *  
from app.email import send_email
from flask_login import login_required, login_user,\
     logout_user, current_user





def send_code_email(user, code):
        """Sending of Welcoming Email for Registrations  """
        send_email(('Complete your registration'),
                sender = formataddr(('Bookify Support', current_app.config['ADMINS'][0] )), 
               recipients=[user.email], 
               text_body=render_template('email/code.html', user=user,code=code ),
               html_body=render_template('email/code.html', user=user,code=code))
        

def send_profile_email(user, grade):
        send_email((f'{user.name.title()}! Your profile looks good!'),
                sender = formataddr(('Bookify Support', current_app.config['ADMINS'][0] )), 
               recipients=[user.email], 
               text_body=render_template('email/profile.html', user=user, grade=grade ),
               html_body=render_template('email/profile.html', user=user, grade=grade))



def send_welcome_email(user):
        send_email((f'{user.name} We are Excited as you are'),
                sender = formataddr(('Bookify Team', current_app.config['ADMINS'][0] )), 
               recipients=[user.email], 
               text_body=render_template('email/welcome_email.txt', user=user, ),
               html_body=render_template('email/welcome_email.html', user=user,))