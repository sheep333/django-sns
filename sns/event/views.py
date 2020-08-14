from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Event


class EventCreateView(CreateView):
    model = Event


class EventDetailView(DetailView):
    model = Event


class EventListView(ListView):
    model = Event


class EventUpdateView(UpdateView):
    model = Event
