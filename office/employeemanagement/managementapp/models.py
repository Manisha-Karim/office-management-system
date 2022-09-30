from django.db import models

class Department(models.Model):
    name= models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Position(models.Model):
    name =models.CharField(max_length = 100, null = False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=30, null = False)
    last_name = models.CharField(max_length=30, null = False)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField(default=5000)
    bonus = models.IntegerField(default=0)
    email = models.CharField(max_length= 50, default= 0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.email)





