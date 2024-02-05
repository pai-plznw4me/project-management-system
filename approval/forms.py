from django import forms

from helper import apply_widget_by_field, get_all_field_info
from .models import Approval

from django import forms


class ApprovalCreateForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields, verbose_names, types = get_all_field_info(model, with_id=False)
        fields_with_id, _ ,_ = get_all_field_info(model, with_id=True)  # foreign key 에 _id 가 붙어 있지 않음
        field_names = verbose_names  # table에 보여질 필드 이름

        widgets = apply_widget_by_field(model,
                                        fields,
                                        DateTime=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
                                        Date=forms.widgets.DateInput(attrs={'type': 'date'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 생성시에 field 을 2개로 제한함. ('REQ', 'REQUEST'), ('EUR', 'Emergency under Review')
        self.fields['status'].choices = Approval.CHOICES[:2]


class ApprovalIndexForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields, verbose_names, types = get_all_field_info(model, with_id=False)
        fields_with_id, _, types = get_all_field_info(model, with_id=True)
        field_names = verbose_names
        widgets = apply_widget_by_field(model,
                                        fields,
                                        DateTime=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
                                        Date=forms.widgets.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ApprovalUpdateForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields, verbose_names, types = get_all_field_info(model, with_id=False)
        field_names = verbose_names
        widgets = apply_widget_by_field(model,
                                        fields,
                                        DateTime=forms.widgets.DateInput(attrs={'type': 'datetime-local'}),
                                        Date=forms.widgets.DateInput(attrs={'type': 'date'}))
        widgets['requester'] = forms.widgets.DateInput(attrs={'readonly': 'readonly'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 생성시에 field 을 2개로 제한함. ('REQ', 'REQUEST'), ('EUR', 'Emergency under Review')
        self.fields['status'].choices = Approval.CHOICES[:2]

