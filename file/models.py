from django.db import models

from file.validators import validate_version_format


# Create your models here.
class File(models.Model):
    # file content
    filecontent = models.FileField()
    # 파일 이름
    name = models.CharField(max_length=100)
    # 파일 설명
    desc = models.TextField(null=True, blank=True)
    # 파일 확장자
    ext = models.CharField(max_length=10, null=True)
    # 파일 용량
    size = models.IntegerField()
    # 문서 업로드 시간
    upload_datetime = models.DateTimeField(auto_now_add=True)
    # 문서 생성 시간
    creation_date = models.DateField(null=True, blank=True)
    # 문서 버전
    version = models.CharField(max_length=100, validators=[validate_version_format], null=True, blank=True)

