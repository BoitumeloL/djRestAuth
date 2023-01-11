from django.shortcuts import render
from django.core.mail import mail_admins
from allauth.account.views import ConfirmEmailView

from dj_rest_auth.registration.views import RegisterView
#from users.customized_serializers import CustomRegisterSerializer

from dj_rest_auth.views import LoginView
from .customized_serializers import CustomLoginSerializer
# Create your views here.

#def get_email(request):
#   email = request.user.email
#  return email

class CustomizedConfirmEmailView(ConfirmEmailView):
    def confirm_email(self, request, email_confirmation, signup=False):
        response = super().confirm_email(request,email_confirmation,signup)
        #username = self.context[request].user

        subject = 'Verification Link Clicked'
        message = f'Hi {request.user.username} has clicked the verification link to verify their email'
        #email_from = 'brethabile25@gmail.com'
        #recipient = [request.user.email,]
        #send_mail(subject, message, email_from, recipient)
        
        mail_admins(subject,message,fail_silently=False,connection=None,html_message=None)

        #send_mail(
        #    'Verification Link Clicked', 
        #    'A user has clicked the verification link to verify their email{}'
        #    .format(email_confirmation.email_address.user),
        #    'brethabile25@gmail.com',
        #    ['brethabile25@gmail.com'],
        #    fail_silently=False,
        #)
        
        return response
    
 
#class CustomRegisterView(RegisterView):
    #serializer_class = CustomRegisterSerializer

class CustomLoginView(LoginView):
    '''
    This is a customized login view that allows the user to login using their email and their password

    '''
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)