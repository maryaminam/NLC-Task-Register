from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Task,Profile
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .forms import TaskForm,EditForm
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def tasks_view(request):
    if request.user.is_authenticated:
        query = request.GET.get('search', '')
        sort_by = request.GET.get('sort_by', 'task')  # Default sorting by task name

        # Check if the user is a manager
        if hasattr(request.user, 'profile') and request.user.profile.is_manager:
            # Get the manager's department
            manager_department = request.user.profile.department

            # Filter tasks by the manager's department
            user_tasks = Task.objects.filter(department=manager_department).order_by(sort_by)
        else:
            # Regular users see only their tasks
            user_tasks = Task.objects.filter(user=request.user).order_by(sort_by)

        # Apply search filter
        if query:
            user_tasks = user_tasks.filter(Q(user__username__icontains=query))

        # Pagination
        paginator = Paginator(user_tasks, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = None

    return render(request, 'home.html', {'page_obj': page_obj, 'query': query, 'sort_by': sort_by})


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Assign the task to the logged-in user
        form.instance.user = self.request.user

        # Set the department of the logged-in user
        if hasattr(self.request.user, 'profile'):
            form.instance.department = self.request.user.profile.department

        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        # Set the initial value for the 'user' field
        initial['user'] = self.request.user
        # Note: 'department' field will be set in form_valid
        return initial

class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('home')

class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('home')
