from django.db import models
from django.contrib.auth.models import User
from event_app.models import Event

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        unique_together = ['user', 'event']

    def __str__(self):
        return f"{self.user.username} booked {self.event.name}"
