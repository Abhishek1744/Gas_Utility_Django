from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'consumer_services'

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-request/', views.submit_service_request, name='submit_request'),
    path('request-status/', views.request_status, name='request_status'),
    path('account-information/', views.account_information, name='account_information'),
    path('request-submitted/', views.request_submitted, name='request_submitted'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name='login'),
]
