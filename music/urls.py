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

urlpatterns += [
    path('performers/create/', views.PerformerCreate.as_view(), name='performer_create'),
    path('performers/<int:pk>/update/', views.PerformerUpdate.as_view(), name='performer_update'),
    path('performers/<int:pk>/delete/', views.PerformerDelete.as_view(), name='performer_delete'),
]

urlpatterns += [
    path('songs/create/', views.SongCreate.as_view(), name='song_create'),
    path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='song_update'),
    path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='song_delete'),
]

