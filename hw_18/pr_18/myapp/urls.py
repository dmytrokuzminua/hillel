from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('password/', views.change_password_view, name='change_password'),
    path('profile/', views.redirect_to_own_profile, name='my_profile_redirect'),
    path('profile/<str:username>/', views.profile_view, name='profile'),

]