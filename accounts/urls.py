from django.urls import path
from .views import login_view, logout_view, signup_view

urlpatterns = [
    path("log-in/", login_view, name="login"),
    path("log-out/", logout_view, name="logout"),
    path("sign-up/", signup_view, name="signup"),
]
