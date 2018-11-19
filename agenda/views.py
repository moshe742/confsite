from django.shortcuts import render
from django.views.generic import View, ListView
from agenda.models import Speaker


# Create your views here.
class SpeakersList(ListView):
    model = Speaker
    template_name = 'agenda/speakers_list.html'

    # def get(self, request, *args, **kwargs):
    #     pass