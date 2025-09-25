from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'position', 'salary', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отчество'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
            'position': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Должность'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Зарплата'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
        }

