from django import forms
from resources.models import Resource
class FormResource(forms.ModelForm):
    created_at = forms.DateTimeField(required=False,disabled=True,widget=forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Created at(is auto generated)'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Resource
        exclude = ('slug',)
        help_texts = {
            'title':'Title the resource',
            'url':'Submit the url of resource',
            'resource_type': 'The type of resourse(Video,Article,Book)',
            'skills': 'The skills for which the resource is:'
        }
        error_messages = {
            'url':{'invalid':'Enter a valid url!','required':'This field is required.'},
            'title':{'max_length':'The title max_contains 100 letters','required':'This field is required.'},
            'resource_type':{'required':'This field is required.'}
        }
        widgets = {
            'skills':forms.CheckboxSelectMultiple,
            'resource_type':forms.Select(attrs={'class':'form-select','placeholder':'Select the type of resourse'}),
            'url':forms.URLInput(attrs={'class':'form-control','placeholder':'Submit the url of resource'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title the resource'}),
        }
        labels = {
            'title':'Title',
            'url':'URL',
            'resource_type':'Resource Type',
            'skills':'Skills'
        }