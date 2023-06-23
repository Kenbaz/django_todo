from django.urls import path
from . import views


urlpatterns = [
    #Add task
    path('addtask/', views.addtask, name='addtask'),
    #Mark task as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    #Unmark task
    path('unmark_task/<int:pk>/', views.unmark_task, name='unmark_task'),
    #Edit task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    #Delete task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task')
]