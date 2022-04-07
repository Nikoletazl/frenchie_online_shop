from django.urls import path

from frenchie_online_shop.web.views import StoreView, HomePageView

urlpatterns = (
    path('store/', StoreView.as_view(), name='store'),
    path('', HomePageView.as_view(), name='home page'),
)