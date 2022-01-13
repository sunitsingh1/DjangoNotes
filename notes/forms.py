from django.core.exceptions import ValidationError
from django import forms 

from .models import Note

class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title','text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control my-5'}),
            'text':forms.Textarea(attrs={'class':'form-control mb-5'})
        }
        labels = {
            'text':"Write your thought here"
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("we only accept notes about Django!")
        return title