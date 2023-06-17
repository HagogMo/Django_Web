from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'commun-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('about/', views.about, name = 'commun-about'),
]