from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_user, name='user-login'),
    path('logout/', LogoutView.as_view(next_page="main-page"), name="user-logout"),
    path('<int:pk>/', views.user_profile, name="user-profile"),
    path('signup/', views.signup, name="user-create"),
    path('<int:pk>/update/', views.user_update, name="user-update"),
]
