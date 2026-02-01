from django import forms
from category.models import Category
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