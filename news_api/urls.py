
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    
    path('home/', views.home, name='home'),
    path('business/', views.business, name='business'),
    path('technology/', views.technology, name='technology'),
    path('health/', views.health, name='health'),
    path('science/', views.science, name='science'),
    path('sports/', views.sports, name='sports'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('general/', views.general, name='general'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
]
