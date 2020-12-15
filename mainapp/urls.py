"""Импортируем классы с class view"""
from django.urls import path
from .views import PostListView, IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index-page'),
]
