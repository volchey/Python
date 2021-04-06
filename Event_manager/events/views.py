from django.shortcuts import render
from datetime import datetime, timedelta
from events.models import Event
from collections import defaultdict

def calendar(request):
    now = datetime.now()
    week_begin = now - timedelta(days=now.weekday())
    week_end = week_begin + timedelta(days=7)

    all_events = Event.objects.filter(starttime__range=[week_begin, week_end], endtime__range=[week_begin, week_end])

    days = [week_begin]
    for i in range(1, 7):
        it_day = week_begin + timedelta(days=i)
        days.append(it_day.replace(hour=0, minute=0, second=0, microsecond=0))

    hours = defaultdict(list)
    for it_hour in range(7, 23):
        for it_day in days:
            it_day_time = it_day + timedelta(hours=it_hour)
            print("it day time: ",it_day_time)

            next_day = it_day + timedelta(days=1)
            if (all_events.filter(starttime__range=[it_day, it_day_time], endtime__range=[it_day_time, next_day]).exists()):
                print(it_day, it_day_time)
                hours[it_hour].append(True)
            else:
                hours[it_hour].append(False)

    print(hours)
    return render(request, 'events/calendar.html', {'hours': hours.items, 'days': days})

def create_event(request):
    return render(request, 'events/create_event.html', {})