from django.urls import path
from .views import activate_key_sent, login_view, logout_view, signup_view, activation_success, activation

urlpatterns = [
    path("log-in/", login_view, name="login"),
    path("log-out/", logout_view, name="logout"),
    path("sign-up/", signup_view, name="signup"),
    path("activation_sent/", activate_key_sent, name="activation_sent"),
    path("activation_success/", activation_success, name="activation_success"),
    path("activate/<str:key>", activation, name="activation"),
]
