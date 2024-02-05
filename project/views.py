from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from approval.forms import ApprovalCreateForm
from approval.models import Approval
from file.forms import FileCreateForm
from project.forms import ProjectCreateForm, ProjectUpdateForm, ProjectFileCreateForm, ProjectFileUpdateForm, \
    ProjectDetailForm, ProjectFileDetailForm
from helper import detail_html, standard_create, standard_update, standard_detail, standard_index, card_row, h_tag, \
    get_base_url, standard_delete, generate_crud_table, generate_crud_filetable, crud_formtable, gantt_crud_formtable, \
    approval_crud_formtable
from project.models import Project, ProjectFile


def index(request):
    """
    프로젝트 목록을 표시하는 인덱스 뷰 함수입니다.

    :param request: HttpRequest 객체
    :return: HttpResponse 객체
    """

    def _callback(**kwargs):
        crud_table_html = kwargs['crud_table_html']
        added_contents = kwargs['added_contents']
        title = h_tag(2, '프로젝트 목록')
        added_contents[0] = title + card_row((crud_table_html, 12))

    return standard_index(request, Project, {}, ProjectCreateForm, 'project', 'doctris', crud_formtable, _callback)


# Create your views here.
@csrf_exempt
def create(request):
    """
    프로젝트를 생성하는 뷰 함수입니다.

    :param request: HttpRequest 객체
    :return: HttpResponse 객체
    """

    def _callback(**kwargs):
        if kwargs['request'].method == 'GET':
            title = h_tag(2, '프로젝트 생성')
            kwargs['added_contents'][0] = title + card_row((kwargs['added_contents'][0], 12))

    return standard_create(request, 'standard/create.html', ProjectCreateForm, 'project:index', {}, 'doctris',
                           _callback)


@csrf_exempt
def projectfile_create(request):
    """
    프로젝트 산출물을 생성하는 뷰 함수입니다.

    :param request: HttpRequest 객체
    :return: HttpResponse 객체
    """

    def _callback(**kwargs):
        if kwargs['request'].method == 'POST':
            valid_inst = kwargs['valid_inst']
            redirect_path_variables = kwargs['redirect_path_variables']
            # 옆 코드를 실행하기 위해 필요한 코드=> redirect(project:detail, id=valid_inst.project_id)
            redirect_path_variables['id'] = valid_inst.project_id
        if kwargs['request'].method == 'GET':
            title = h_tag(2, '프로젝트 산출물 생성')
            kwargs['added_contents'][0] = title + card_row((kwargs['added_contents'][0], 12))

    return standard_create(request, 'standard/create.html', ProjectFileCreateForm, 'project:detail', {}, 'doctris',
                           _callback)


def update(request, id):
    """
    프로젝트를 업데이트하는 뷰 함수입니다.

    :param request: HttpRequest 객체
    :param id: 프로젝트의 식별자
    :return: HttpResponse 객체
    """

    def _callback(**kwargs):
        if kwargs['request'].method == 'GET':
            title = h_tag(2, '프로젝트 업데이트')
            kwargs['added_contents'][0] = title + card_row((kwargs['added_contents'][0], 12))

    return standard_update(request, id, 'standard/update.html', Project, ProjectUpdateForm, 'project:index', None,
                           'doctris', _callback)


def projectfile_update(request, id):
    """
    프로젝트 산출물을 업데이트하는 뷰 함수입니다.

    :param request: HttpRequest 객체
    :param id: 산출물의 식별자
    :return: HttpResponse 객체
    """

    def _callback(**kwargs):
        if kwargs['request'].method == 'POST':
            valid_inst = kwargs['valid_inst']
            redirect_path_variables = kwargs['redirect_path_variables']
            redirect_path_variables[
                'id'] = valid_inst.project_id  # => redirect(project:detail, id=valid_inst.project_id)
        if kwargs['request'].method == 'GET':
            title = h_tag(2, '산출물 업데이트')
            kwargs['added_contents'][0] = title + card_row((kwargs['added_contents'][0], 12))

    return standard_update(request, id, 'standard/update.html', ProjectFile, ProjectFileUpdateForm, 'project:detail',
                           {}, 'doctris', _callback)


def detail(request, id):
    """
    프로젝트 상세 정보를 보여주는 뷰 함수입니다.

    :param request: HttpRequest 객체
    :param id: 프로젝트의 식별자
    :return: HttpResponse 객체
    """

    def _callback(**kwargs):
        # Detail cabllback function 기본 인자.
        base_url = get_base_url(kwargs['request'].build_absolute_uri())
        inst = kwargs['instance']
        detail_content = kwargs['detail_content']
        added_contents = kwargs['added_contents']  # added_contents is list, list is mutable!

        # 프로젝트 상세 설명
        project_title = h_tag(2, '프로젝트 상세')  # h2 tag 제목
        added_contents[0] = project_title + card_row((detail_content, 12))  # added_contents 내 첫번째 요소 : detail_content

        # 프로젝트 산출물
        # CRUD 테이블을 생성헙니다.
        projectfiles = ProjectFile.objects.filter(project=inst)
        crud_projectfile_table = crud_formtable(base_url, projectfiles, ProjectFileCreateForm, 'project/projectfile')
        projectfile_title = h_tag(2, '프로젝트 산출물 관리')  # h2 tag 제목
        added_contents.append(projectfile_title + card_row((crud_projectfile_table, 12)))

        # WBS 산출물
        projectfile_title = h_tag(2, 'WBS')  # h2 tag 제목
        wbs_projectfiles = projectfiles.filter(output='BD14-2')
        crud_wbs_table = gantt_crud_formtable(base_url, wbs_projectfiles, ProjectFileCreateForm, 'project/projectfile', target_colname='output')
        added_contents.append(projectfile_title + card_row((crud_wbs_table, 12)))

        # 구매 관리 산출물
        approvals = Approval.objects.filter(project=inst)
        approval_title = h_tag(2, '구매 관리')  # h2 tag 제목
        approval_crud_table = approval_crud_formtable(base_url, approvals, ApprovalCreateForm, 'approval')
        added_contents.append(approval_title + card_row((approval_crud_table, 12)))

        # 계약 관리 산출물
        projectfile_title = h_tag(2, '계약 관리')  # h2 tag 제목
        added_contents.append(projectfile_title + card_row((crud_projectfile_table, 12)))

        # 계약 관리 산출물
        projectfile_title = h_tag(2, '계약관리')  # h2 tag 제목
        added_contents.append(projectfile_title + card_row((crud_projectfile_table, 12)))

        # 자산 관리 산출물
        projectfile_title = h_tag(2, '자산관리')  # h2 tag 제목
        added_contents.append(projectfile_title + card_row((crud_projectfile_table, 12)))


    return standard_detail(request, id, Project, ProjectDetailForm, 'doctris', _callback)


def projectfile_detail(request, id):
    """
    프로젝트 산출물 상세 정보를 보여주는 뷰 함수입니다.

    :param request: HttpRequest 객체
    :param id: 산출물의 식별자
    :return: HttpResponse 객체
    """

    def _callback(**kwargs):
        inst = kwargs['instance']
        if inst.output == 'BD14-2':
            print('this is wbs')

        detail_content = kwargs['detail_content']
        added_contents = kwargs['added_contents']  # added_contents is list, list is mutable!
        file = inst.file
        file_detail_content = detail_html(request, file, FileCreateForm)

        # card 태그를 Wrapping 합니다.
        projectfile_title = h_tag(2, '프로젝트 산출물 상세')  # h2 tag 제목
        added_contents[0] = projectfile_title + card_row(
            (detail_content, 12))  # added_contents 내 첫번째 요소 : detail_content
        file_title = h_tag(2, '파일 설명')  # h2 tag 제목
        added_contents.append(card_row((file_title + file_detail_content, 12)))

    return standard_detail(request, id, ProjectFile, ProjectFileDetailForm, 'doctris', _callback)


def delete(request, id):
    """
    프로젝트를 삭제하는 뷰 함수입니다.

    :param request: HttpRequest 객체
    :param id: 프로젝트의 식별자
    :return: HttpResponse 객체
    """
    return standard_delete(request, id, Project, 'project:index', {}, None)


def projectfile_delete(request, id):
    """
    프로젝트 산출물을 삭제하는 뷰 함수입니다.

    :param request: HttpRequest 객체
    :param id: 산출물의 식별자
    :return: HttpResponse 객체
    """

    def _callback(**kwargs):
        if kwargs['instance'].file:
            kwargs['instance'].file.delete()
        kwargs['redirect_path_variables']['id'] = kwargs['instance'].project.id

    return standard_delete(request, id, ProjectFile, 'project:detail', {}, _callback)
