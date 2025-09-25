from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'phone', 'position', 'email', 'salary', 'date_hired')
    search_fields = ('first_name', 'last_name', 'middle_name', 'position', 'email')
