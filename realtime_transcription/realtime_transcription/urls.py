from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('realtime/', include('transcript.urls')),
    path('user/', include('user.urls')),
]
