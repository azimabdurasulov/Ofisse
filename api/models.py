from django.db import models

class Deperment(models.Model):
    name = models.CharField(max_length=100)
    location= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    dept = models.ForeignKey(Deperment, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.phone}'