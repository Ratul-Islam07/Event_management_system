from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from event_app.models import Event
from django.contrib import messages

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # booking limit set
    booking_count = Booking.objects.filter(event=event).count()
    if booking_count >= 3:
        return render(request, 'booking_app/fully_booked.html') 

    Booking.objects.create(user=request.user, event=event)
    messages.success(request, "Your booking was successful!")
    return redirect('homepage') 


@login_required
def booked_events(request):
    bookings = Booking.objects.filter(user=request.user).select_related('event')
    booked_events = [booking.event for booking in bookings] 
    return render(request, 'booking_app/booked_events.html', {'booked_events': booked_events})

@login_required
def unbook_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    booking = Booking.objects.filter(user=request.user, event=event).first()

    if booking:
        booking.delete()
    
    return redirect('booked_events')  

