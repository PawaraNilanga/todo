from django.urls import path
from pyexpat import features

from . import views

urlpatterns = [
    # add Task
    path('addTask/', views.addTask, name='addTask'),

    # mark as done
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),

    # mark as un done
    path('mark_as_undone/<int:pk>/',views.mark_as_undone, name='mark_as_undone'),

    # edit features
    path('edit_task/<int:pk>/',views.edit_task, name='edit_task'),

    # Delete Task
    path('delete_task/<int:pk>/',views.delete_task, name='delete_task'),
]