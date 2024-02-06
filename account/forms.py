from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    회원 가입시 사용하는 ModelForm
    """
    class Meta:
        model = CustomUser
        # 회원 가입 페이지에서 보여줄 기본 유저 필드
        base_field = ['username',
                      'first_name',
                      'last_name',
                      'email',
                      'password1',
                      'password2',
                      ]

        # 회원 가입 페이지에서 보여줄 커스텀 유저 필드
        custom_field = ['phone_number',
                        'career',
                        'rank',
                        'date_company_joined',
                        'personal_id',
                        'company_id',
                        'department',
                        'resume',
                        'id_photo',
                        'region']
        fields = tuple(base_field + custom_field)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # null=True로 설정한 필드에 대해 required를 False로 설정
        self.fields['resume'].required = False
        self.fields['id_photo'].required = False


class CustomUserProfileForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # 회원 가입 페이지에서 보여줄 기본 유저 필드
        base_field = ['username',
                      'first_name',
                      'last_name',
                      'email',
                      ]

        # 회원 가입 페이지에서 보여줄 커스텀 유저 필드
        custom_field = ['phone_number',
                        'career',
                        'rank',
                        'date_company_joined',
                        'personal_id',
                        'company_id',
                        'department',
                        'resume',
                        'id_photo',
                        'region']
        fields = tuple(base_field + custom_field)
