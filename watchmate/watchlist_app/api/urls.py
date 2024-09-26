from django.urls import path
from .views import watch_list,watchlist_detail,stream_platform,stream_platform_detail,ReviewList,ReviewDetail,ReviewCreate
urlpatterns = [
    path('list', watch_list, name='movie-list'),
    path('<int:pk>', watchlist_detail, name='movie-detail'),

    path('stream', stream_platform, name='stream-platform'),
    path('stream/<int:pk>', stream_platform_detail, name='stream-platform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list'),  #review for a particular movie
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'), # access individual review 
    
]
