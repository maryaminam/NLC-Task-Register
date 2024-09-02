from django import forms
from .models import Task, Category, Service

# Get choices from the database
choices = Category.objects.all().values_list('category', 'category')
choices2 = Service.objects.all().values_list('service', 'service')

# Convert queryset to a list for choices
choice_list = list(choices)
choice_list2 = list(choices2)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('user', 'task', 'start_date', 'service_key', 'category_key')
        labels = {
            'service_key': 'Service',  # Change label
            'category_key': 'Category',  # Change label
        }

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'id': 'maryam', 'type': 'hidden'}),
            'task': forms.TextInput(attrs={'class': 'form-control','placeholder':'Task'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            #'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'service_key': forms.Select(choices=choice_list2, attrs={'class': 'form-control'}),
            'category_key': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model= Task
        fields = ('user', 'task', 'start_date', 'service_key', 'category_key')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'id': 'maryam', 'type': 'hidden'}),
            'task': forms.TextInput(attrs={'class': 'form-control','placeholder':'Task'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            #'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'service_key': forms.Select(choices=choice_list2, attrs={'class': 'form-control'}),
            'category_key': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }
