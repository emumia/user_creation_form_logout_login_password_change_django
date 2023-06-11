from django.urls import path
from . import views

urlpatterns = [
    path("usercform/", views.usercform,name='registration'),
    path("login/", views.login_form,name='login'),
    path("success/", views.slogin),
    path("logout/", views.logout_form,name='logout'),
    path("passc/", views.password_change,name='passwordchange'),
    path("withoutoldpassc/", views.without_old_password_change,name='withoutoldpassc'),
    
]