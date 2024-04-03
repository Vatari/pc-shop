from django.urls import path

from shop.accounts.views import LoginUserView, RegisterUserView, CustomLogoutView

urlpatterns = (
    path("login/", LoginUserView.as_view(), name="login"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
)