from django.contrib import admin
from .models import Department ,Doctor , Profile , Patient , appointment
# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Profile)
admin.site.register(appointment)