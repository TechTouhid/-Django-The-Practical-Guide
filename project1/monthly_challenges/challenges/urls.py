from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.january),
    path("", views.index), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),  # for the int value in url
    # <month> is a place holder for different values of url
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
