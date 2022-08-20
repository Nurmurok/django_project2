from django.urls import path
from .views import PostListView, PostCreateViews, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('create/', PostCreateViews.as_view(), name='blog-create'),
    path('post/<int:pk>', PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
]

