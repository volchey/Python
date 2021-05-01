from django.shortcuts import render
from datetime import date, datetime, timedelta, time
from django.utils import timezone
from events.models import Event, Subject, Location
from collections import defaultdict
from django.views.generic.edit import CreateView

def daterange_gen(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def calendar(request):
    now = timezone.now()

    daterange = request.GET.get('daterange')

    print(daterange)

    start_end_range = daterange.split(' - ', 1) if daterange else list()

    start_date_str = start_end_range[0] if start_end_range else ''
    end_date_str = start_end_range[1] if start_end_range else ''

    start_date = datetime.strptime(start_date_str, '%m/%d/%Y') if start_date_str else now
    end_date = datetime.strptime(end_date_str, '%m/%d/%Y') if end_date_str else now + timedelta(days=7)

    print(start_date, end_date)
    all_subjects_ids = Event.objects.filter(starttime__range=[start_date, end_date]).values_list('subject', flat=True).distinct()

    all_subjects = Subject.objects.filter(id__in=all_subjects_ids)

    enabled_subjects_ids = set()
    for it_subject in all_subjects:
        it_subject.enabled = False
        if request.GET.get(it_subject.description) != '0':
            it_subject.enabled = True
            enabled_subjects_ids.add(it_subject.id)

    all_location_ids = Event.objects.filter(starttime__range=[start_date, end_date]).values_list('location', flat=True).distinct()

    all_locations = Location.objects.filter(id__in=all_location_ids)

    enabled_location_ids = set()
    for it_location in all_locations:
        it_location.enabled = False
        if request.GET.get(it_location.name) != '0':
            it_location.enabled = True
            enabled_location_ids.add(it_location.id)

    days = dict()
    for curr_day in daterange_gen(start_date, end_date):
        day_min = datetime.combine(curr_day, time.min)
        day_max = datetime.combine(curr_day, time.max)
        curr_events = Event.objects.filter(
            starttime__range=[day_min, day_max],
            subject__id__in=enabled_subjects_ids,
            location__id__in=enabled_location_ids
            ).order_by('starttime')

        days[curr_day] = curr_events

    return render(request, 'calendar.html', {
        'days': days, 'start_date': start_date, 'end_date': end_date,
        'subjects': all_subjects,
        'locations': all_locations})

class EventCreate(CreateView):
    template_name = 'event_form.html'
    model = Event
    fields = '__all__'