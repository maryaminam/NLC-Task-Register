from django.urls import path,include

from .views import tasks_view,AddTaskView,UpdateTaskView,DeleteTaskView

urlpatterns = [
    path('', tasks_view,name='home'),
    path('add_task',AddTaskView.as_view(),name='add_task'),
    path('edit_task/<int:pk>/', UpdateTaskView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
    #path('', TaskView ,name='tasks'),
]