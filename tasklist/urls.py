from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('update/<int:task_id>', views.update, name='update'),
    path('delete/<int:task_id>', views.destroy, name='destroy'),
]