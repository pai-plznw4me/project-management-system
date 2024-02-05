from django import forms

from helper import get_all_field_info
from .models import File


class FileCreateForm(forms.ModelForm):
    class Meta:
        model = File
        remove = ['name', 'ext', 'size', 'upload_datetime']
        fields, verbose_names, types = get_all_field_info(model, with_foreignkey=True, with_id=False, remove=remove)
        fields_with_id, _, _ = get_all_field_info(model, with_foreignkey=True, with_id=True, remove=remove)
        field_names = verbose_names

        widgets = {
            'creation_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FileUpdateForm(forms.ModelForm):
    class Meta:
        model = File
        remove = ['name', 'ext', 'size', 'upload_datetime']
        fields, verbose_names, types = get_all_field_info(model, with_foreignkey=True, with_id=False, remove=remove)
        fields_with_id, _, _ = get_all_field_info(model, with_foreignkey=True, with_id=True, remove=remove)
        field_names = verbose_names

        widgets = {
            'creation_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
