from django.urls import path
from . import views


urlpatterns = [
    path("departments", views.ListDepartments.as_view()),
    path("employees", views.ListEmployees.as_view()),
]
