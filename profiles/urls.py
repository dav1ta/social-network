from django.urls import path
from .views import UserLoginView,UserLogoutView,UserRegisterView,UserUpdateView,AddFriendsView,FriendListView,UserProfile

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('update/<int:pk>/',UserUpdateView.as_view(),name='update'),
    path('profile/<int:pk>/',UserProfile.as_view(),name='profile'),
    path('add_friends/',AddFriendsView.as_view(),name='add_friends'),
    path('friends/',FriendListView.as_view(),name='friends'),
    ]
