from django.contrib import admin
from .models import ServiceRequest
from .models import Customer

admin.site.register(ServiceRequest)
admin.site.register(Customer)

