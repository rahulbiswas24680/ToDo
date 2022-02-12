from django.urls import path
from .views import middle, task_detail, create_task, update_task, delete_task


urlpatterns = [
    path('', middle, name='middle'),        #get all tasks
    path('task/<int:task_id>/', task_detail, name='task-detail'),       #task_detaail view
    path('task/create/', create_task, name="create-task"),        # create task
    path('task/update/<int:task_id>', update_task, name="update-task"),       # update task
    path('task/delete/<int:task_id>', delete_task, name="delete-task")        # delete task
]
