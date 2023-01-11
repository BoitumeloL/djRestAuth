from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView
from allauth.account.views import ConfirmEmailView 
from users.views import CustomizedConfirmEmailView, CustomLoginView

from .views import CustomLoginView

urlpatterns = [
   
    #path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('account/confirm-email/<key>/', CustomizedConfirmEmailView.as_view(), name='account_confirm_email'),
    #path('custom-register/',CustomRegisterView.as_view()),
    path('register/', RegisterView.as_view()),
    
    path('login/', CustomLoginView.as_view(), name='rest_login'),

    #path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    #re_path('account-confirm-email/<key>/',
         #VerifyEmailView.as_view(), name='account_confirm_email'),
    
]