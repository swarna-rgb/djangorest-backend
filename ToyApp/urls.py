from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('toys/', views.ToyList.as_view(), name='toy_list'),
    path('mtoys/', views.ToyListMixins.as_view(), name='toy_list_mixin'),
    path('mtoys/<int:id>/', views.ToyDetailMixins.as_view(), name='toy_detail_mix'),
    path('toys/<int:id>/', views.ToyDetail.as_view(), name='toy_detail'),
    path('gtoys/', views.GenericToyList.as_view(), name='generic_toy_list'),
    path('gtoys/<int:pk>/', views.GenericToyDetail.as_view(), name='generic_toy_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)