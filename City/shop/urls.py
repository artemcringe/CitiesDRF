from django.urls import path, include

from . import views

urlpatterns = [
    path('city/', views.CityLISTAPIView.as_view(), name='city-list'),
    path('city/<int:pk>/', views.CityRetrieveAPIView.as_view(), name='city-detail'),
    path('city/<int:pk>/street/', views.StreetListAPIView.as_view(), name='city-streets'),
    path('shop/', views.ShopCreateAPIView.as_view(), name='shop-list_or_create'),
    # path('')
]
