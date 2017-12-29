from django import forms

from .models import Tweet


class TweetModelForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                    attrs={'placeholder': 'Message title',
                                           'class': 'form-control'}
                                ))
    text = forms.CharField(label='',
                            widget=forms.Textarea(
                                    attrs={'rows': 3,
                                           'style':'resize:none;overflow:hidden',
                                           'placeholder': 'Your message',
                                           'class': 'form-control'}
                                ))

    class Meta:
        model = Tweet
        fields = [
            'title',
            'text'
        ]
        # exclude = ['user']

    # def clean_text(self, *args, **kwargs):
    #     text = self.cleaned_data.get('text')
    #     if text == 'abc':
    #         raise forms.ValidationError('Cannot be ABC')
    #     return text