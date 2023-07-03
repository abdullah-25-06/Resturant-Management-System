from django.urls import path
from . import views


app_name='customer'

urlpatterns = [
    path('',views.login1,name='login1'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout1,name='logout'),
]