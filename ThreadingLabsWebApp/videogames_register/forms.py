from django import forms
from .models import VideoGame

from videogames_register.models import VideoGame


class VideoGameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        fields = ('title', 'genre', 'description', 'release_date')
        labels = {
            'title': 'title',
            'release_Date': 'release Date'
        }

    def __init__(self, *args, **kwargs):
        super(VideoGameForm,self).__init__(*args, **kwargs)
        self.fields['genre'].empty_label = "Select"
        self.fields['release_date'].required = False




