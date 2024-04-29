from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .models import Customer
from .forms import ServiceRequestForm, CustomerUpdateForm

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

@login_required
def request_tracking(request):
    customer_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'request_tracking.html', {'customer_requests': customer_requests})

@login_required
def update_customer_profile(request):
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=request.user.customer)
        if form.is_valid():
            form.save()
            return redirect('request_tracking')
    else:
        form = CustomerUpdateForm(instance=request.user.customer)
    return render(request, 'update_customer_profile.html', {'form': form})



# Create your views here.
