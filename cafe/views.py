from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Menu, Event
from .forms import InquiryForm


# Create your views here.
def index(request):
    return render(request, 'cafe/index.html')


def event(request):
    events = Event.objects.filter(end_event_date__gte=timezone.now())
    return render(request, 'cafe/event.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'cafe/event_detail.html', {'event': event})


def store(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
        return render_to_response('cafe/store.html', {'message': '감사합니다. 빠른 시일내에 답변 드리겠습니다.',
                                                      'form': InquiryForm()})
    else:
        form = InquiryForm()
    return render(request, 'cafe/store.html', {'form': form})


def menu(request):
    tropical_revolutions = Menu.objects.filter(category='Tropical Revolution')
    ice_flakes = Menu.objects.filter(category='Ice Flakes')
    coffee = Menu.objects.filter(category='Coffee')
    menu_list = [coffee, ice_flakes, tropical_revolutions]
    return render(request, 'cafe/menu.html', {'menu_list': menu_list})


def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'cafe/menu_detail.html', {'menu': menu})



