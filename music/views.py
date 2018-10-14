from django.forms import ModelForm, forms
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .models import Performer, Song


# def index(request):                             # just the very first version; to be replaced at a later stage
#     return HttpResponse("<h1>Because the night "
#                         "belongs to lovers...</h1>")


def index(request):
    num_performers = Performer.objects.all().count()
    num_songs = Song.objects.all().count()
    context = {
        'num_performers': num_performers,
        'num_songs': num_songs,
    }
    return render(request, 'index.html', context=context)


class PerformerListView(generic.ListView):
    model = Performer
    template_name = 'music/performer_list.html'
    paginate_by = 2                             # set to 2 to see the actual effects of pagination

    def get_queryset(self):                     # get list by overriding ListView.get_queryset(); this is typically done
        return Performer.objects.all()          # get all performers initially; objects.filter(...) can be used later


class PerformerDetailView(generic.DetailView):
    model = Performer


class SongListView(generic.ListView):
    model = Song
    template_name = 'music/song_list.html'
    # paginate_by = 2                             # set to 2 to see the actual effects of pagination

    def get_queryset(self):                     # get list by overriding ListView.get_queryset(); this is typically done
        return Song.objects.all()               # get all songs initially; objects.filter(...) can be used later


class SongDetailView(generic.DetailView):
    model = Song


class PerformerCreate(generic.CreateView):
    model = Performer
    fields = '__all__'
    # initial = {'is_band': False}


class PerformerUpdate(generic.UpdateView):
    model = Performer
    fields = ['name', 'is_band']


class PerformerDelete(generic.DeleteView):
    model = Performer
    success_url = reverse_lazy('performer-list')


class SongCreate(generic.CreateView):
    model = Song
    fields = '__all__'


class SongUpdate(generic.UpdateView):
    model = Song
    fields = ['title', 'time', 'performer', 'release_date']


class SongDelete(generic.DeleteView):
    model = Song
    success_url = reverse_lazy('song-list')


