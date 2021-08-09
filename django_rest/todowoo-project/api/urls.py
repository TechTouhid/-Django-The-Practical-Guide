from django.urls import path
from . import views
urlpatterns = [
    path("todos/completed", views.TodoCompleted.as_view()),  # we used as_view() cause we are using classBased view
    path("todos/<int:pk>", views.TodoRetrieveUpdateDestroyAPIView.as_view()),  # using this url we'll view, update and delete data
    path("todos/<int:pk>/complete", views.TodoComplete.as_view()),  # using this url we'll view, update and delete data
    path("todos", views.TodoListCrete.as_view()),  # using this url we are going to create and list todos
]