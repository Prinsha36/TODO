
from django.urls import path
from todo_app import views

urlpatterns = [
    
    path("", views.todo_list,name="todo-list"),
    path("delete/<int:pk>/", views.todo_delete,name="todo-delete"),
    path("create/", views.todo_create,name="todo-create"),
    path("update/<int:pk>/", views.todo_update,name="todo-update"),
]
