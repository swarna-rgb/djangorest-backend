from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('otoys/', views.ToyList.as_view(), name='toy_list'),
    path('mtoys/', views.ToyListMixins.as_view(), name='toy_list_mixin'),
    path('mtoys/<int:id>/', views.ToyDetailMixins.as_view(), name='toy_detail_mix'),
    path('otoys/<int:id>/', views.ToyDetail.as_view(), name='toy_detail'),
    path('toys/', views.GenericToyList.as_view(), name='generic_toy_list'),
    path('toys/<int:pk>/', views.GenericToyDetail.as_view(), name='generic_toy_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.Test_view.as_view(), name='test'),
    path('products/',views.ProductList.as_view(), name='product_list' ),
    path('products/<str:slug>/',views.ProductDetail.as_view(), name='product_detail' )
]

urlpatterns = format_suffix_patterns(urlpatterns)