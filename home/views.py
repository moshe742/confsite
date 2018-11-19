from django.shortcuts import render
from django.views.generic import View
from home.forms import SpeakerForm, PresentationForm, ContactInfoForm


class Home(View):
    def get(self, request):
        return render(request, 'home/home.html', context={'title': 'home',
                                                          'speaker_form': SpeakerForm,
                                                          'presentation_form': PresentationForm,
                                                          'contact_info_form': ContactInfoForm
                                                          })

    def post(self, request):
        pass
