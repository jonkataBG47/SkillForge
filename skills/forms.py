from django import forms
from skills.models import Skill
class FormCategory(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].disabled = True
        self.fields['updated_at'].disabled = True
    class Meta:
        model = Category
        exclude = ('slug',)
        help_texts = {'name':'Give the category a name.','description':'Describe the category(is optional)'}
        error_messages = {
            'name':{'max_length':'The title max_contains 100 letters','required':'This field is required.',
                    'unique':'A skill with this title already exists'},
        }
class FormSkill(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].disabled = True
        self.fields['slug'].disabled = True
        self.fields['updated_at'].disabled = True
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
            'description':'Describe the skill(is optional)',
            'difficulty':'Select the difficulty level.',
            'estimated_hours':'Determine the time it will take you to learn the skill',
            'category':'Which category does the skill belong to?'
        }


