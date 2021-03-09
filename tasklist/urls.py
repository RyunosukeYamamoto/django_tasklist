from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_list, name='user_list'),
    path('user/add/', views.user_edit, name='user_add'),
    path('user/mod/<int:user_id>/', views.user_edit, name='user_mod'),
    path('user/del/<int:user_id>/', views.user_del, name='user_del'),
    path('task/<int:user_id>/', views.TaskList.as_view(), name='task_list'),
    path('task/add/<int:user_id>/', views.task_edit, name='task_add'),
    path('task/mod/<int:user_id>/<int:task_id>/', views.task_edit, name='task_mod'),
    path('task/del/<int:user_id>/<int:task_id>/', views.task_del, name='task_del'),
]