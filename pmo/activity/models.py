from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

# Create your models here.
class Department(models.Model):
    dept_manager = models.ForeignKey(User,on_delete=CASCADE)
    dept_name= models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


# models.py
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.user.username



class Service(models.Model):
    service = models.CharField(max_length=255)

    def __str__(self):
        return self.service

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


# models.py
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(auto_now_add=True)
    service_key = models.ForeignKey(Service, on_delete=models.CASCADE)
    category_key = models.ForeignKey(Category, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)  # New field

    def __str__(self):
        return self.task + ' | ' + str(self.user)



