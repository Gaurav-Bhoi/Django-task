from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('signup', views.signup),
    path('sendotp', views.send_otp),
    path('verifyOtp', views.verifyOtp),
    path('login_request', views.login_request),
    path('complete', views.complete),
    path('uploadProfile', views.uploadProfile)

]
