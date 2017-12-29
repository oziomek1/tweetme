from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
# Create your models here.


from .validators import validate_text

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=120, validators=[validate_text])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("tweet:detail",  kwargs={'pk': self.pk})

    # def clean(self, *args, **kwargs):
    #     text = self.text
    #     if text == 'abc':
    #         raise ValidationError('Cannot be ABC')
    #     return super(Tweet, self).clean(*args, **kwargs)
