from django.urls import path
from .views import watch_list,watchlist_detail,stream_platform,stream_platform_detail
urlpatterns = [
    path('list', watch_list, name='movie-list'),
    path('<int:pk>', watchlist_detail, name='movie-detail'),
    path('stream', stream_platform, name='stream-platform'),
    path('stream/<int:pk>', stream_platform_detail, name='stream-platform-detail'),
    
]
