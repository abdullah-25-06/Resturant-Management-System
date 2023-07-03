from . import views
from django.urls import path

app_name = 'canteen'
urlpatterns = [
    path('',views.index,name='index'),
    path('order/<int:id>',views.Order,name='order')
]