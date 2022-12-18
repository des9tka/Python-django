from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class EmailService:

    @staticmethod
    def __send_email(to: str, templates_name: str, context: dict, subject=''):
        template = get_template(templates_name)
        html_content = template.render(context)
        massage = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        massage.attach_alternative(html_content, "text/html")
        massage.send()

    @classmethod
    def register_email(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email(user.email, 'register.html', {'name': user.profile.name, 'url': url}, 'Register')

    @classmethod
    def recovery_password_by_email(cls, user):
        token = JWTService.create_token(user, RecoveryToken)
        url = f'http://localhost:3000/recovery/{token}'
        cls.__send_email(user.email, 'recovery.html', {'url': url, 'name': user.profile.name}, 'Recovery Password')
