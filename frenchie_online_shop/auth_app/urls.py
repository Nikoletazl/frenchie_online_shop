from django.urls import path

from frenchie_online_shop.auth_app.views import UserRegistrationView, UserLoginView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
)