from django.contrib import admin
from .models import StudentRegister,FacultyRegister

# Register your models here.
admin.site.register(StudentRegister)
admin.site.register(FacultyRegister)