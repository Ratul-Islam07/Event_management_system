from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('events/', include('event_app.urls')),
    path('bookings/', include('booking_app.urls')),
    path('', include('homepage_app.urls')),
]
