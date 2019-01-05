from django.forms import ModelForm, HiddenInput
from agenda.models import Speaker, Presentation, ContactInfo


class PresentationForm(ModelForm):
    class Meta:
        model = Presentation
        fields = ('title', 'abstract')


class SpeakerForm(ModelForm):
    class Meta:
        model = Speaker
        fields = ('user', 'bio')
        widgets = {
            'user': HiddenInput()
        }


class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        fields = ('info_type', 'info', 'speaker')
        widgets = {
            'speaker': HiddenInput()
        }
