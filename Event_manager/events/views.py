from django.shortcuts import render
from datetime import date, datetime, timedelta, time
from django.utils import timezone
from events.models import Event
from collections import defaultdict
from django.views.generic.edit import CreateView

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def calendar(request):
    now = timezone.now()

    start_date_str = request.GET.get('start_date', '')
    end_date_str = request.GET.get('end_date', '')

    start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else now
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else now + timedelta(days=7)

    all_subjects = Event.objects.filter(starttime__range=[start_date, end_date]).values_list('subject').distinct()

    print(all_subjects)

    days = dict()
    subjects = set()
    for curr_day in daterange(start_date, end_date):
        day_min = datetime.combine(curr_day, time.min)
        day_max = datetime.combine(curr_day, time.max)
        curr_events = Event.objects.filter(starttime__range=[day_min, day_max]).order_by('starttime')

        days[curr_day] = curr_events

        for it_event in curr_events:
            subjects.add(it_event.subject.description)

    return render(request, 'events/calendar.html', {'days': days, 'start_date': start_date, 'end_date': end_date, 'subjects': subjects})

class EventCreate(CreateView):
    model = Event
    fields = '__all__'