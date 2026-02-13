from django import forms
from learning_paths.models import LearningPath
class FormLearningPaths(forms.ModelForm):
    created_at = forms.DateTimeField(required=False,disabled=True,widget=forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Created at(is auto generated)'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = LearningPath
        exclude = ('slug',)
        help_texts ={
            'title':'Title the the learning path',
            'description':'Write your plan',
            'skills':'The skills for which the learning paths is:',
        }
        error_messages = {
            'title':{'max_length':'The title max_contains 255 letters',
                     'required':'This field is required.',
                    'unique':'A learning path with this title already exists'},
            'description':{'required':'This field is required.'},
            'skills': {'required':'This field is required.'}
        }
        widgets = {
            'skills':forms.CheckboxSelectMultiple(),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title the the learning path'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Write your plan'}),
        }
        labels = {
            'title':'Title',
            'description':'Description',
            'skills':'Skills'
        }