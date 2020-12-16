from django.urls import path
from .views import BlogListView, BlogDetailView 

#I am following directions in the Django for Beginners (3.1) book, by William S. Vincent - Hexx King

urlpatterns = [
  path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
  path('', BlogListView.as_view(), name='home'),
]