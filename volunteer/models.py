from django.db import models
from django.conf import settings
from django import forms
from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse





class VolunteerEvent(models.Model):

    # tags_choices =[
    #     ('HOME_REPAIR', 'Home Repair'), 
    #     ('BAKE_SALE', 'Bake Sale')
    # ]

    event_title = models.CharField(max_length=25)
    event_datetime = models.DateTimeField(default=datetime(2020, 1, 1))
    event_description = models.CharField(max_length=250)
    # event_tags = models.CharField(max_length=15, choices=tags_choices, null=True, blank=True)
    cover = models.ImageField(upload_to='images/', blank=False, null=False, default="stock/thomas.jpg")
    event_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    attending=models.ManyToManyField(User, related_name='events_attending')
    #slug=models.SlugField(null=True)
    def __str__(self):
        return self.event_title
    #def get_absolute_url(self):
     #   return reverse('event_detail', kwargs={'slug': self.slug})

