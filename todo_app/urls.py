from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("signup", views.signup),
    path("signin", views.signin),
    path("logout", views.logout),
    path("lists", views.lists),
    path("todo/<str:id>", views.tasks),
    path("task/<str:id>", views.is_done),
    path("task/delete/<str:id>", views.task_delete),
    path("todo/add_task/<str:id>", views.add_task),
    path("add_list", views.add_list),
   
]