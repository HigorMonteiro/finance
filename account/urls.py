from django.urls import path, include
from account import views
from rest_framework import routers

#RegisterView, LoadUserView
router = routers.DefaultRouter()
router.register(r'register', views.RegisterView, 'register')
router.register(r'login', views.LoadUserView, 'login')

urlpatterns = [
    path("v1/auth/", include(router.urls)),

]