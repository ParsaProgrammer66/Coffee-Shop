from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('edit_profile/',views.edit_profile,name='edit'),
    path('delete/', views.delete_user, name='delete'),
]
