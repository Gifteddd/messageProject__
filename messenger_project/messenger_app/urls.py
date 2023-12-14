from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

from .views import *

urlpatterns = [
    path('', views.rooms),
    path("<str:slug>/", views.room, name="room"),
    path("api/rooms/", RoomAPIView.as_view()),
    path("api/rooms/<int:pk>/", RoomDetailAPIView.as_view()),
    path("api/messages/", MessageAPIView.as_view()),
    path('profile', profile_view, name="profile"),
    path("<str:slug>/create_message/", create_message, name="create_message"),
    path("<str:slug>/delete_message/<int:message_id>/", delete_message, name="delete_message"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)