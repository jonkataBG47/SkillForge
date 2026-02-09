from django.core.exceptions import ValidationError
def blank_validator(value):
    if not value.strip():
        raise ValidationError('This field cannot be blank or contain only whitespace.')