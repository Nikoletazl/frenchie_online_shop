from django.urls import path

from frenchie_online_shop.auth_app.views import UserRegistrationView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register'),
)