from django.urls import path
from .views import PostCreateView , PostListview,PostDetailView,PostRemoveView

urlpatterns = [
    # path('',PostListView.as_view(),name='posts'),
    path('create/',PostCreateView.as_view(),name='post_create'),
    path('feed/',PostListview.as_view(),name='posts'),
    path('post/<pk>',PostDetailView.as_view(),name='post'),
    path('delete/<pk>',PostRemoveView.as_view(),name='post_delete'),
    ]
