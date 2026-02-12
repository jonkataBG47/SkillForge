from skills.models import Skill
from django import forms
class FormSkill(forms.ModelForm):
    #created_at = forms.DateTimeField(required=False,disabled=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for created_at in self.fields:
        #     self.fields[created_at].widget.attrs['readonly'] = 'readonly'
        #     self.fields[created_at].required = False
    class Meta:
        model = Skill
        exclude = ('slug',)
        error_messages = {
            'title':{'max_length':'The title max_contains 255 letters',
                     'required':'This field is required.',
                    'unique':'The category already exists'},
            'difficulty':{'required':'This field is required.'},
            'estimated_hours':{'required':'This field is required.',},
            'category':{'required':'This field is required.!'}
        }
        help_texts = {
            'title':'Title the skill',
            'description':'Describe the skill',
            'difficulty':'Select the difficulty level.',
            'estimated_hours':'Determine the time it will take you to learn the skill',
            'category':'Which category does the skill belong to?'
        }
        widgets = {
            'difficulty':forms.Select(attrs={'class':'form-select'}),
        }


