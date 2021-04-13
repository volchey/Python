from django.shortcuts import render
from datetime import datetime, timedelta, time
from django.utils import timezone
from events.models import Event
from collections import defaultdict
from django.views.generic.edit import CreateView

def calendar(request):
    now = timezone.now()
    # week_begin = now - timedelta(days=now.weekday())
    # all_events = Event.objects.filter(starttime__range=[now.date(), next_days_range.date()])

    days = dict()
    for i in range(0, 7):
        curr_day = now + timedelta(days=i)
        day_min = datetime.combine(curr_day, time.min)
        day_max = datetime.combine(curr_day, time.max)
        print(day_min, day_max)
        curr_events = Event.objects.filter(starttime__range=[day_min, day_max])

        days[curr_day] = curr_events

    #     it_day = week_begin + timedelta(days=i)
    #     days.append(it_day.replace(hour=0, minute=0, second=0, microsecond=0))

    # hours = defaultdict(list)
    # for it_hour in range(7, 23):
    #     for it_day in days:
    #         it_day_time = it_day + timedelta(hours=it_hour)
    #         print("it day time: ",it_day_time)

    #         next_day = it_day + timedelta(days=1)
    #         if (all_events.filter(starttime__range=[it_day, it_day_time], endtime__range=[it_day_time, next_day]).exists()):
    #             print(it_day, it_day_time)
    #             hours[it_hour].append(True)
    #         else:
    #             hours[it_hour].append(False)

    # print(all_events.query)
    return render(request, 'events/calendar.html', {'days': days})

class EventCreate(CreateView):
    model = Event
    fields = '__all__'