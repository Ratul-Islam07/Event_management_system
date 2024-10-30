from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:event_id>/', views.book_event, name='book_event'),
    path('booked/', views.booked_events, name='booked_events'),
    path('unbook/<int:event_id>/', views.unbook_event, name='unbook_event'),
]
