from django.contrib import admin

# Register your models here.
from .models import Assignment,SubmitAssignment


admin.site.register(Assignment)
admin.site.register(SubmitAssignment)