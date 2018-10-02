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

