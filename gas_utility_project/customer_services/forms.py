from django import forms
from .models import ServiceRequest
from .models import Customer

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone_number', 'address']
