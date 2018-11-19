from django.shortcuts import render
from django.views.generic import View, ListView


# Create your views here.
class SponsorsList(ListView):
    def get(self, request, *args, **kwargs):
        pass
