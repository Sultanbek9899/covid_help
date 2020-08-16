from django import forms
from .models import Help_request


class Help_requestForm(forms.ModelForm):
    class Meta:
        model = Help_request
        fields = ('name', 'help_type', 'number', 'city', 'info')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}),
            'info': forms.Textarea(attrs={'placeholder': 'Чем вы можете помочь?',
                                          'class': 'form-control'}),
            'number': forms.TextInput(attrs={'placeholder': "Прим. 0999112233",
                                             'class': 'form-control'}),
            'city': forms.TextInput(
                attrs={'placeholder': 'Город/село', 'class': 'form-control'}),
        }

