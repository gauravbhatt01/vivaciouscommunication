from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='viv-home'),
    path('details/', views.details, name='viv-details'),
    path('reviews/', views.reviews, name='viv-reviews'),
    path('certificate/', views.certificate, name='viv-cert'),
    path('sign-in/', views.signin, name='viv-signin'),
    path('sign-up/', views.signup, name='viv-signup'),
]