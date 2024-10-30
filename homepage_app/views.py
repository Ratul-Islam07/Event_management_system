from django.shortcuts import render
from event_app.models import Event
from booking_app.models import Booking
from django.shortcuts import render
from event_app.models import Event, Category
from booking_app.models import Booking 
from datetime import datetime
from django.db.models import Q


def homepage(request):
    # Get the search query and selected category from GET parameters
    search_query = request.GET.get('query', '') 
    selected_category_id = request.GET.get('category')  
    
    categories = Category.objects.all()

    events = Event.objects.all()

    # Apply the search filter
    if search_query:
        try:
            search_date = datetime.strptime(search_query, '%Y-%m-%d').date()
            events = events.filter(date=search_date)
        except ValueError:
            events = events.filter(
                Q(name__icontains=search_query) | Q(location__icontains=search_query)
            )

    # Apply category filter if selected
    if selected_category_id:
        events = events.filter(category_id=selected_category_id)

    # Get event IDs booked by the logged-in user
    user_bookings = []
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user).values_list('event_id', flat=True)
    
    # Pass search query and selected category ID to keep them persistent in the response
    return render(request, 'homepage_app/homepage.html', {
        'events': events,
        'categories': categories,
        'selected_category_id': selected_category_id,
        'search_query': search_query,
        'user_bookings': user_bookings,
    })



