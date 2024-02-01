from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser): # <-- 상속 부분
    phone_number = models.CharField(max_length=11)  # 전화번호(char)
    career = models.IntegerField()  # 경력 (int)
    rank = models.CharField(max_length=10)  # 직급 (select)
    date_company_joined = models.DateField()  # 입사 기간
    id_number = models.CharField(max_length=13)  # 주민등록번호
    department = models.CharField(max_length=13)  # 부서
    resume = models.FileField(blank=True, null=True)  # 이력서
    id_photo = models.ImageField(blank=True, null=True, upload_to='')  # 증명사진
    region = models.CharField(max_length=100)  # 주소

    def __str__(self):
        return self.username

