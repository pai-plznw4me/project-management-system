from django import forms
from django.utils import timezone
from file.models import File
from helper import apply_widget_by_field, get_all_field_info, extract_file_info
from project.models import Project, ProjectFile


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        # 모델의 모든 필드 가져옴
        fields, verbose_names, types = get_all_field_info(model, with_foreignkey=True, remove=['file'], with_id=False)
        fields_with_id, _, _ = get_all_field_info(model, with_foreignkey=True, remove=['file'], with_id=True)
        field_names = verbose_names

        widgets = {
            'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'end_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class ProjectFileCreateForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        # 모델의 모든 필드 가져옴, foreinkey 는 제외함
        remove = ['name',
                  'ext',
                  'size',
                  'upload_datetime']
        fields, verbose_names, types = get_all_field_info(model, with_foreignkey=True, with_id=False, remove=remove)
        fields_with_id, _, _ = get_all_field_info(model, with_foreignkey=True, with_id=True, remove=remove)
        field_names = verbose_names  # table에 보여질 필드 이름

        # 필드 별로 지정된 위젯을 적용,
        widgets = apply_widget_by_field(ProjectFile,
                                        fields,
                                        Date=forms.widgets.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def save(self, commit=True):
        # ProjectFile 에 file 객체 추가
        projectfile = super().save(commit=False)

        # file 정보를 추출해 instance 에 추가
        filecontent = self.cleaned_data['filecontent']
        info = extract_file_info(filecontent)
        projectfile.name = info['name']
        projectfile.ext = info['ext']
        projectfile.size = info['size']
        current_time = timezone.now()
        projectfile.upload_datetime = current_time
        projectfile.save()
        return projectfile


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        # 모델의 일부 필드만 가져올시 아래 코드 해제
        # fields = ['id',
        #           'name',
        #           'alias',
        #           'start_date',
        #           'end_date']

        fields, verbose_names, types = get_all_field_info(model, with_foreignkey=True, remove=['file'], with_id=False)
        fields_with_id, _, _ = get_all_field_info(model, with_foreignkey=True, remove=['file'], with_id=True)
        field_names = verbose_names
        widgets = {
            'id': forms.widgets.DateInput(attrs={'readonly': 'readonly'}),
            'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'end_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProjectFileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields, verbose_names, types = get_all_field_info(model, with_foreignkey=True, remove=['file'], with_id=False)
        fields_with_id, _, _ = get_all_field_info(model, with_foreignkey=True, remove=['file'], with_id=True)
        field_names = verbose_names

        widgets = apply_widget_by_field(ProjectFile,
                                        fields,
                                        Date=forms.widgets.DateInput(attrs={'type': 'date'}))

        widgets['id'] = forms.widgets.DateInput(attrs={'readonly': 'readonly'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProjectDetailForm(forms.ModelForm):
    class Meta:
        model = Project
        # 모델의 일부 필드만 가져올시 아래 코드 해제
        # fields = ['id',
        #           'name',
        #           'alias',
        #           'start_date',
        #           'end_date']

        # 모델의 모든 필드 가져옴
        fields, verbose_names, types = get_all_field_info(model, with_foreignkey=True, remove=['file'], with_id=False)
        fields_with_id, _, _ = get_all_field_info(model, with_foreignkey=True, remove=['file'], with_id=True)
        field_names = verbose_names
        # 모든 필드를 readonly 로 함
        widgets = {field: forms.widgets.TextInput(attrs={'readonly': 'readonly'}) for field in fields}
        # widgets = {
        #     'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        #     'end_date': forms.widgets.DateInput(attrs={'type': 'date'})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProjectFileDetailForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        # 모델의 모든 필드 가져옴
        fields, verbose_names, types = get_all_field_info(model, with_foreignkey=True, with_id=False)
        fields_with_id, _, _ = get_all_field_info(model, with_foreignkey=True, with_id=True)
        field_names = verbose_names
        widgets = apply_widget_by_field(ProjectFile,
                                        fields,
                                        Date=forms.widgets.DateInput(attrs={'type': 'date'}))
        # 모든 필드를 readonly 로 함
        widgets = {field: forms.widgets.TextInput(attrs={'readonly': 'readonly'}) for field in fields}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
