from django.forms import ModelForm
from django import forms
from .models import Song , Review


# <<!--class SongForm(ModelForm):
#     class Meta:
#         model = Song
#         fields = ['name', 'singer','image', 'song','tags']
#
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }
#
#     def __init__(self, *args , **kwargs):
#         super(SongForm, self).__init__(*args, **kwargs)
#
#         self.fields['name']

class reviewForm(ModelForm):
    class Meta:
        model=Review
        fields = ['value','body']


        labels = {

           'value':'place your vote!',
           'body':'add a comment with your vote'
        }

    def __init__(self , *args , **kwargs):
        super(reviewForm,self).__init__(*args, **kwargs)

        self.fields['value'].widget.attrs.update({'class':'input'})
        self.fields['body'].widget.attrs.update({'class': 'input'})