from django.urls import path
from .views import list_tasks, create_task,delete_task, update_task

urlpatterns =[
    path('',list_tasks),
    path('new/',create_task),
    path('delete_task/<int:task_codigo>/',delete_task,name='delete_task'),
    path('update_task/<int:task_codigo>/', update_task, name='update_task'),
    
]