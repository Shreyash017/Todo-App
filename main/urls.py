from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('todos/', views.todoList, name="todoList"),
    path('todos/<int:pk>', views.todoUpdate, name="todoUpdate"),
    path('DELETE/todos/<int:pk>', views.todoDelete, name="todoDelete"),
]