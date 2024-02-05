from django.db import models
from account.models import CustomUser
from project.models import Project


# Create your models here.
# TODO : 추후 Company 분리하기
class Approval(models.Model):
    requester = models.ForeignKey(to=CustomUser, on_delete=models.SET_NULL, null=True, verbose_name='요청자')
    name = models.CharField(max_length=100, verbose_name='제목')
    desc = models.TextField(verbose_name='구매 사유')
    link = models.TextField(verbose_name='링크')
    project = models.ForeignKey(to=Project, on_delete=models.SET_NULL, null=True)
    INOUT_CHOICES = [('IN', "구매"), ('OT', '판매')]
    inout = models.TextField(verbose_name='매입 | 매출', choices=INOUT_CHOICES)
    request_datetime = models.DateTimeField(verbose_name='요청 시간')
    approval_date = models.DateField('승인 시간')
    CHOICES = [('REQ', 'REQUEST'), ('EUR', 'Emergency under Review'), ('UDR', 'Under review'), ('CPL', 'COMPLETE')]
    status = models.CharField(max_length=3, choices=CHOICES, default='UDR', verbose_name='승인 상태')
    purchase = models.CharField(max_length=100, verbose_name='판매 회사')
    sales = models.CharField(max_length=100, verbose_name='구매 회사')
    delivery = models.CharField(max_length=100, verbose_name='배송지')
    quantity = models.PositiveIntegerField(default=1, verbose_name='주문 수량')
    price = models.PositiveIntegerField(default=0, verbose_name='주문 가격')

    class Meta:
        permissions = [('can_approval',  # 기록될 권한 이름
                        'Can approval')]  # 사용자에게 보여질 권한 이름