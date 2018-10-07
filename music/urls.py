"""The URLconfig of the music app."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('performers/', views.PerformerListView.as_view(), name='performer-list')
]

urlpatterns += [
    path('performers/<int:pk>/', views.PerformerDetailView.as_view(), name='performer-detail')
]

urlpatterns += [
    path('songs/', views.SongListView.as_view(), name='song-list')
]

urlpatterns += [
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song-detail')
]

