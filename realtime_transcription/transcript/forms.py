from django import forms
from .models import Meetings


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meetings
        fields = ['meeting_name']