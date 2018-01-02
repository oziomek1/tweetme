from django.urls import path

from .views import (
    TweetListAPIView,
    TweetCreateAPIView,
    RetweetAPIView,
    LikeToggleAPIView,
    TweetDetailAPIView
    )

app_name = 'tweet-api'
urlpatterns = [
    # path('', RedirectView.as_view(url='/')),
    path('', TweetListAPIView.as_view(), name='list'),  # /api/tweet/
    # path('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path('create/', TweetCreateAPIView.as_view(), name='create'),  # /api/tweet/create/
    # path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', TweetDeleteView.as_view(), name='date')
    path('<int:pk>/retweet/', RetweetAPIView.as_view(), name='retweet'),
    path('<int:pk>/like/', LikeToggleAPIView.as_view(), name='like'),
    path('<int:pk>/', TweetDetailAPIView.as_view(), name='detail'),
]
