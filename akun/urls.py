from django.urls import path
app_name = 'akun'
from .views import (
    registerPage, 
    loginPage, 
    logoutUser, 
    set_apd,
    detail_apd,
    list_apd
)

urlpatterns = [
    path('apd/', set_apd, name="apd"),
    path('daftar_rs/', list_apd, name="daftar_rs"),
    path('<int:id>/', detail_apd, name="detail-apd"),
    path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),  
	path('logout/', logoutUser, name="logout")
]