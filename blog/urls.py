from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    UpdateSeatsAPI,
)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/update_seats/<int:pk>', UpdateSeatsAPI.as_view(), name='update-seats-api'),
]
