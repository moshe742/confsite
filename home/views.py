from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from agenda.forms import SpeakerForm, PresentationForm
from agenda.models import Speaker


class Home(View):
    def get(self, request):
        return render(request, 'home/home.html')

    def post(self, request):
        data = request.POST
        user = request.user
        speaker = Speaker.objects.filter(user=user).first()
        if speaker:
            presentation_form = PresentationForm(data)
            if presentation_form.is_valid():
                presentation = presentation_form.save()
                speaker.sessions.add(presentation)
                speaker.save()
                return render(request, 'home/home.html', context={'title': 'home- it works'})
        speaker_form = SpeakerForm(data)
        presentation_form = PresentationForm(data)

        if speaker_form.is_valid() and presentation_form.is_valid():
            presentation = presentation_form.save()
            speaker = speaker_form.save()
            speaker.sessions.add(presentation)
            speaker.save()
            return render(request, 'home/home.html', context={'title': 'home- works'})
