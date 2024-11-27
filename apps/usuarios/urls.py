from django.urls import path
from apps.usuarios.views import     cadastro,login,logout,ative,dashboard


urlpatterns = [
    path('cadastr',cadastro,name='cadastro'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    path('dashboard',dashboard,name='dashboard'),
    path('ative/<uidb64>/<token>/',ative,name='ative'),
]