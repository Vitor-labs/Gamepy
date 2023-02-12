"""Email sending by parallel threads"""
import threading

from django.core.mail import EmailMessage


class EmailThread(threading.Thread):
    """Parallel Thread Creator"""
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Utils:
    """It's util"""
    @staticmethod
    def send_email(data):
        """Email notification definition"""
        email = EmailMessage(
            subject=data['email_subject'], 
            body=data['email_body'], 
            to=[data['to_email']])
        EmailThread(email).start()
