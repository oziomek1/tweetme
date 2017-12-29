from django.core.exceptions import ValidationError


def validate_text(value):
    text = value
    if text == '':
        raise ValidationError('Text cannot be blank')
    return value