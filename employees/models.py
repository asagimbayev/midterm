from django.db import models

# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"