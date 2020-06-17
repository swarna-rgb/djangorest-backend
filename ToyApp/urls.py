from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('toys/', views.toy_list, name='toy_list'),
    path('toys/<int:id>/', views.toy_detail, name='toy_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)