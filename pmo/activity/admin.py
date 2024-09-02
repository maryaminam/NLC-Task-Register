from django.contrib import admin
from .models import Task,Service,Category,Department,Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Department)
