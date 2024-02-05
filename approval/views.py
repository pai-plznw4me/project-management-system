from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from approval.forms import ApprovalUpdateForm, ApprovalIndexForm, ApprovalCreateForm
from approval.models import Approval
from helper import h_tag, card_row, standard_index, standard_detail, standard_create, standard_update, standard_delete, \
    approval_crud_formtable


def index(request):
    return standard_index(request, Approval, {}, ApprovalIndexForm, 'approval', 'doctris',
                          approval_crud_formtable, None)


@csrf_exempt
def create(request):
    return standard_create(request, 'standard/create.html', ApprovalCreateForm, 'approval:index', {}, 'doctris', None)


def detail(request, id):
    return standard_detail(request, id, Approval, ApprovalIndexForm, 'doctris', None)


def update(request, id):
    def _callback(**kwargs):
        if kwargs['request'].method == 'GET':
            title = h_tag(2, '프로젝트 업데이트')
            kwargs['added_contents'][0] = title + card_row((kwargs['added_contents'][0], 12))

    return standard_update(request,
                           id,
                           'standard/update.html',
                           Approval,
                           ApprovalUpdateForm,
                           'approval:index',
                           None,
                           'doctris', _callback)


def delete(request, id):
    return standard_delete(request, id, Approval, 'approval:index', {}, None)


# TODO: ajax로 변경하기
@permission_required('approval.can_approval', 'approval:not_approval')
def approval(request, id):
    inst = Approval.objects.get(id=id)
    if inst.status == 'REQ':
        inst.status = 'UDR'
        inst.save()
    elif inst.status == 'UDR':
        inst.status = 'CPL'
        inst.save()
    elif inst.status == 'CPL':
        inst.status = 'UDR'
        inst.save()
    else:
        raise NotImplementedError
    previous_page = request.META.get('HTTP_REFERER', '/')
    return redirect(previous_page)

# TODO: ajax 로 변경하기
def not_approval(request):
    def _callback(**kwargs):
        kwargs['added_contents'].append('검토 및 승인 권한이 없습니다')
        print(request.user.user_permissions.all())
        kwargs['added_contents'].append(str(request.user.user_permissions.all()))

    return standard_index(request, Approval, {}, ApprovalIndexForm, 'approval', 'doctris',
                          approval_crud_formtable, _callback)
