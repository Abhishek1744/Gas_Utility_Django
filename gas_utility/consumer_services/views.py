from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, AccountInformation
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

def allow_all_users(view_func):
    def wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return user_passes_test(lambda u: True)(wrapper)

def home(request):
    return render(request, 'consumer_services/home.html')

@allow_all_users
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            if request.user.is_authenticated:
                service_request.user = request.user
            service_request.save()
            return redirect(reverse('consumer_services:request_submitted'))
    else:
        form = ServiceRequestForm()
    return render(request, 'consumer_services/submit_request.html', {'form': form})

# @allow_all_users
# def request_status(request):
#     if isinstance(request.user, AnonymousUser):
#         # Handle unauthenticated users
#         # You can either redirect them to the login page or display a message
#         return redirect('login_url')
    
#     service_requests = ServiceRequest.objects.filter(user=request.user)
#     return render(request, 'consumer_services/request_status.html', {'service_requests': service_requests})
@login_required
def request_status(request):
    service_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'consumer_services/request_status.html', {'service_requests': service_requests})

@allow_all_users
def account_information(request):
    account_info = AccountInformation.objects.get(user=request.user)
    return render(request, 'consumer_services/account_information.html', {'account_info': account_info})

def request_submitted(request):
    return render(request, 'consumer_services/request_submitted.html')