from django.urls import path
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import MediaList,StreamList, MediaDetail, \
    StreamDetail, ReviewCreate, MediaReviewList, MediaReviewDetail


urlpatterns = [
    path("media/", MediaList.as_view(), name="media_list"),
    path("media/<int:pk>/", MediaDetail.as_view(), name="media_detail"),

    path("media/<int:pk>/review-create/", ReviewCreate.as_view(), name="review_create"),
    path("media/<int:pk>/review-list/", MediaReviewList.as_view(), name="review_list"),
    path("media/<int:pk>/review-edit/", MediaReviewDetail.as_view(), name="review-edit"),

    path("stream/", StreamList.as_view(), name= "stream_list"),
    path("stream/<int:pk>/", StreamDetail.as_view(), name="stream_detail")
]