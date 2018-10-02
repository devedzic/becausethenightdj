from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import generic

from .models import Performer


def index(request):
    return HttpResponse("<h1>Because the night belongs to lovers...</h1>")


class PerformerListView(generic.ListView):
    model = Performer
    template_name = 'music/performer_list.html'
    # paginate_by = 2                             # set to 2 to see the actual effects of pagination

    def get_queryset(self):                     # get list by overriding ListView.get_queryset(); this is typically done
        return Performer.objects.all()          # get all performers initially; objects.filter(...) can be used later


class PerformerDetailView(generic.DetailView):
    model = Performer


