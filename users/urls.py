from  django.urls import path

from . import views
from .views import Userlogin, register,login

urlpatterns=[ 
    
    path('register/',register,name='register'),
    path('Userlogin/',Userlogin,name='login'),
    path('logout/',views.logout_user,name='logout')


]