
from .views import common,home
from django.urls import path
app_name="Home"
urlpatterns = [
        path('',home,name='Home'),
        path('common/',common),
]