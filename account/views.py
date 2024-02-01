from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from account.forms import CustomUserCreationForm, CustomUserProfileForm
from account.models import CustomUser


# Create your views here.
def index(request):
    HttpResponse('Hello')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  # <-- FILES 와 같이 입력이 되어야 한다.
        if form.is_valid():
            # file field 데이터 저장
            inst = form.save(commit=False)

            # file field 데이터 저장
            id_photo = form.cleaned_data['id_photo']
            inst.id_photo.save(id_photo.name, id_photo)

            # 일반 form data 저장
            inst.save()

            # profile 페이지로 redirect 함
            return HttpResponse('Signup complete')
        else:
            print('Errors:', form.errors)
            return render(request, template_name='account/signup.html', context={'errors': form.errors})

    elif request.method == 'GET':
        form = CustomUserCreationForm()  # <-바뀐 부분
        return render(request, template_name='account/signup.html', context={'form': form})

    else:
        raise NotImplementedError


@csrf_exempt
def profile(request):
    user = CustomUser.objects.get(username=request.user)

    # field 이름을 추출합니다.
    field_names = CustomUserProfileForm.Meta.fields
    # field 별 type 을 추출합니다.
    types = []
    for name in field_names:
        field = user._meta.get_field(name)
        # field 가 Image type 이면 'ImageType' 으로 타입을 저장합니다.
        # 모델 필드의 내부 타입은 실제 데이터베이스에서 사용되는 타입입니다.
        # get_internal_type()으로 반환되는 값은 FileField 입니다.
        if isinstance(field, models.ImageField):
            types.append('ImageField')
        else:
            types.append(field.get_internal_type())
    # template 을 rendering 합니다.
    context = {'user': user, 'field_names': field_names, 'types': types}
    return render(request, template_name='account/profile.html', context=context)


