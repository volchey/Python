from django.shortcuts import render
from datetime import datetime, timedelta

def calendar(request):
    dt = datetime.now()
    start = dt - timedelta(days=dt.weekday())
    days = [start.strftime('%A %d/%m')]

    for i in range(1, 7):
        it_day = start + timedelta(days=i)
        days.append(it_day.strftime('%A %d/%m'))

    return render(request, 'events/calendar.html', {'range': range(7, 23), 'days': days})

def create_event(request):
    return render(request, 'events/create_event.html', {})