from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_form,name="form"),
    path("successfully/", views.success,name="successfully"),
]