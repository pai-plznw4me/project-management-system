from django import forms
from .models import File


class FileCreateForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['filecontent',
                  'desc',
                  'creation_date',
                  'version']

        widgets = {
            'creation_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FileUpdateForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['filecontent',
                  'desc',
                  'creation_date',
                  'version']

        widgets = {
            'creation_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
