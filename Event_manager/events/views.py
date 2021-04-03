from django.shortcuts import render

def calendar(request):
    return render(request, 'events/calendar.html', {'range': range(7, 23)})

def create_event(request):
    return render(request, 'events/create_event.html', {})