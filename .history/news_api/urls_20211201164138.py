
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import AddFollower, UserSearch, RemoveFollower, ProfileView, ProfileEditView

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    # path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('home/', views.homeDB, name = 'home'),
    path('profile/<int:pk>/', views.keyword),
    path('keyword/', views.keywordDB, name = 'keyword'),
    path('business/', views.businessDB, name = 'business'),
    path('sports/', views.sportsDB, name = 'sports'),
    path('technology/', views.technologyDB, name = 'technology'),
    path('science/', views.scienceDB, name = 'science'),
    path('entertainment/', views.entertainmentDB, name = 'entertainment'),
    path('health/', views.healthDB, name = 'health'),
    path('Liked/', views.like_unlike_post, name = 'like-post-view'),

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

    path('search/', UserSearch.as_view(), name='profile-search'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
]
