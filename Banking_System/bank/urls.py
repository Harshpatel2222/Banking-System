from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_view, name='index'), 
    path('new_customer/',views.new_customer, name='new_customer'), 
]