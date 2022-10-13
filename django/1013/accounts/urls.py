from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("<int:pk>", views.detail, name="detail"),
    path("signup/", views.signup, name="signup"),
    path("update/", views.update, name="update"),
    path("list/", views.list, name="list"),
    path("logout/", views.logout, name="logout"),
    path("password/", views.change_password, name="change_password"),
]
