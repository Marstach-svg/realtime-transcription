from django.urls import path
from .view import meeting_view, transcript_view

urlpatterns = [
    path('meeting/', meeting_view, name="meeting")
    path('transcript/', transcript_view, name="transcript")
]