from django.urls import path
from .import views

urlpatterns=[
    path('master',views.djangoo_master,name='master'),
    path('home',views.djangoo_home,name='home'),
    path('about',views.djangoo_about,name='about'),
    path('contact',views.djangoo_contact,name='contact'),

]