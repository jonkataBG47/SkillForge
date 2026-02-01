from django import forms
from learning_paths.models import LearningPath
class FormLearningPaths(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].disabled = True
        self.fields['updated_at'].disabled = True
    class Meta:
        model = LearningPath
        exclude = ('slug')
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