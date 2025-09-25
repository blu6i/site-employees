from django.db import models


class Employee(models.Model):
    POSITIONS = [
        ('manager', 'Менеджер'),
        ('developer', 'Разработчик'),
        ('designer', 'Дизайнер'),
        ('qa', 'Тестировщик'),
        ('hr', 'HR'),
    ]
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    middle_name = models.CharField("Отчество", max_length=30, null=True, blank=True)
    phone = models.CharField("Номер телефона", max_length=12)
    email = models.EmailField("Электронная почта", unique=True)
    position = models.CharField("Должность", max_length=128, choices=POSITIONS)
    salary = models.DecimalField("Зарплата", max_digits=10, decimal_places=2)
    date_hired = models.DateField("Дата приема на работу", auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.last_name or ""} - {self.position}"