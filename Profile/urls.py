from django.urls import path
from .views import *
app_name='profile'
urlpatterns = [
    path('profile/',complete_profile,name='profile')
]