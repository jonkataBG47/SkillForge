from category.models import Category
from skills.models import Skill
from django import forms
class FormSkill(forms.ModelForm):
    created_at = forms.DateTimeField(required=False,disabled=True,widget=forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Created at(is auto generated)'}))
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user).order_by('-created_at','name')
    class Meta:
        model = Skill
        exclude = ('slug','user')
        error_messages = {
            'title':{'max_length':'The title max_contains 255 letters',
                     'required':'This field is required.',
                    'unique':'This title of skill already exists'},
            'difficulty':{'required':'This field is required.'},
            'estimated_hours':{'required':'This field is required.',},
            'category':{'required':'This field is required!'}
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
            'category':forms.Select(attrs={'class':'form-select'}),
            'estimated_hours':forms.NumberInput(attrs={'class':'form-control','placeholder':'Determine the time it will take you to learn the skill'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title the skill'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Describe the skill'}),
        }
        labels = {
            'title':'Title',
            'description':'Description',
            'difficulty':'Difficulty',
            'estimated_hours':'Estimated Hours',
            'category':'Category'
        }


