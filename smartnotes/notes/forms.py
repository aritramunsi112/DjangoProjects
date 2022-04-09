from cProfile import label
from pyexpat import model
from re import A
from tkinter import Widget
from xml.dom import ValidationErr
from attr import field
from django import  forms


from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=('title','text')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control my-5'}),
            'text':forms.Textarea(attrs={'class':'form-control mb-5'})
        }
        labels={
            'text':'Write your thoughts here',

        }

    def clean_title(self):
        title=self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('we only accept notes about Django')
        return title
