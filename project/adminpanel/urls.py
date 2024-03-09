
from django.urls import path,include
from .views import *

urlpatterns = [

 # Admin Part
    path("adminpage/",adminpage,name='adminpage'),
    path('viewuser/',viewuser,name='viewuser'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name="delete"),
    path('update_product/',update_product,name='update_product'),
    path('allorder/',allorder,name='allorder'),
]