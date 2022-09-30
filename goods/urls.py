from django.urls import path
from goods.views import MainPageView, paintings_shop_view, PaintingDetailView, painting_create_view

urlpatterns = [
    path("", MainPageView.as_view(), name="home"),
    path("shop/", paintings_shop_view, name="shop"),
    path("shop/<slug:slug>/", PaintingDetailView.as_view(), name="painting_detail"),
    path("shop/create", painting_create_view, name="painting_create"),
]
