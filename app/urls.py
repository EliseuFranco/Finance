from django.contrib import admin
from django.urls import path
from finance.views import *
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('expense', expense, name='expense'),
    path('login', login, name='login'),
    path('register/', register,name='register'),
    path('logout/', logout_view, name='logout'),
    path('', lambda request: redirect('index', permanent=True)),
]

