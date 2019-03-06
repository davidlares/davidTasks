from flask_mail import Message
from flask import current_app, render_template
from threading import Thread
from . import mail, app

def send_async_email(message):
    with app.app_context(): # you be sended using the app context
        # send instruction
        mail.send(message)

def welcome_email(user):
    # structure
    message = Message('Welcome to DavidTask', sender=current_app.config['MAIL_USERNAME'], recipients=[user.email])
    # content
    message.html = render_template('email/welcome.html', user=user)
    # secondary process func call
    thread = Thread(target=send_async_email, args=[message])
    thread.start()
