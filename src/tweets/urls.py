from django.urls import path
from django.views.generic import RedirectView

from .views import (
    TweetDetailView,
    TweetListView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView,
    RetweetView
    )

app_name = 'tweets'
urlpatterns = [
    # Home page
    path('', RedirectView.as_view(url='/')),  # /tweet/
    path('search', TweetListView.as_view(), name='list'),  # /tweet/search/
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='date'),
    path('<int:pk>/retweet/', RetweetView.as_view(), name='detail'),
]
