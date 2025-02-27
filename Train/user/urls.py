from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('', views.UserList.as_view(), name='users_list'),
]
