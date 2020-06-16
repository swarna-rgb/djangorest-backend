from django.urls import path
from . import views
urlpatterns = [
    path('toys/', views.toy_list, name='toy_list'),
    path('toys/<int:id>/', views.toy_detail, name='toy_detail')
]