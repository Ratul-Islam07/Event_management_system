from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Category
from .forms import EventForm

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('homepage')
        else:
            print(form.errors) 
    else:
        form = EventForm()
    return render(request, 'event_app/create_event.html', {'form': form})


@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Check if the user is either the creator or a superuser
    if event.created_by != request.user and not request.user.is_superuser:
        return redirect('homepage')  # Or return a forbidden response

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = EventForm(instance=event)
    
    return render(request, 'event_app/update_event.html', {'form': form})
@login_required
def delete_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)
    
    if event.created_by != request.user and not request.user.is_staff:
        return redirect('homepage')

    if request.method == 'POST':
        event.delete()
        return redirect('homepage') 

    # Render the delete confirmation page if GET request
    return render(request, 'event_app/delete_event.html', {'event': event})
