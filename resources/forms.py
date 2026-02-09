from django import forms
from resources.models import Resource
class FormResource(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].disabled = True
        self.fields['updated_at'].disabled = True
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