"""Models related to the music app."""


import datetime

from django.db import models
from django.urls import reverse


class Performer(models.Model):
    """The model representing performers."""

    musician_or_band = [
        [False, 'musician'],
        [True, 'band']
    ]

    name = models.CharField(max_length=100)
    is_band = models.BooleanField(verbose_name="Musician/Band",
                                  choices=musician_or_band,
                                  default=False)

    def __str__(self):
        return self.name + ' (band)' if self.is_band else self.name + ' (musician)'

    def get_absolute_url(self):
        """
        Returns the url to access a particular performer instance.
        Enables specific Performer pages in admin to include "View on site" button.
        """

        return reverse('performer-detail', args=[str(self.id)])


class Song(models.Model):
    """The model representing songs."""

    title = models.CharField(max_length=100)
    time = models.TimeField(null=True, blank=True,
                            default=datetime.time(minute=3, second=0))
    performer = models.ForeignKey(Performer,
                                  on_delete=models.SET_NULL,
                                  null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)

    def format_release_date(self):
        """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'."""

        if isinstance(self.release_date, datetime.date):
            return self.release_date.strftime("%b %d, %Y")
        else:
            return 'unknown'

    def __str__(self):
        return 'song: ' + self.title + '\n' + \
               '\t' + 'performer: ' + (self.performer.name if self.performer else 'unknown') + '\n' + \
               '\t' + 'time: ' + str(self.time) + '\n' + \
               '\t' + 'released: ' + str(self.release_date)

    def get_absolute_url(self):
        """
        Returns the url to access a particular song instance.
        Enables specific Song pages in admin to include "View on site" button.
        """

        return reverse('song-detail', args=[str(self.id)])

