import os.path
from file.forms import FileCreateForm, FileUpdateForm
from file.models import File
from helper import h_tag, card_row, standard_index, generate_crud_filetable, standard_detail, standard_create, \
    standard_update, standard_delete


def index(request):
    return standard_index(request, File, {}, FileCreateForm, 'file', 'doctris', generate_crud_filetable, None,  target_colname='filecontent')


def create(request):
    def _callback(**kwargs):
        if request.method == 'POST':
            valid_inst = kwargs['valid_inst']
            file = valid_inst.filecontent
            file_ext = os.path.splitext(file.name)[1]

            # 속성 정보 저장
            valid_inst.name = file.name
            valid_inst.size = file.size
            valid_inst.ext = file_ext

            # file field 파일 저장
            valid_inst.filecontent.save(file.name, file)

    return standard_create(request, 'standard/create.html', FileCreateForm, 'file:index', {}, 'doctris', _callback)


def detail(request, id):
    return standard_detail(request, id, File, None, 'doctris')


def update(request, id):
    def _callback(**kwargs):
        if kwargs['request'].method == 'GET':
            title = h_tag(2, '파일 업데이트')
            kwargs['added_contents'][0] = title + card_row((kwargs['added_contents'][0], 12))

    return standard_update(request,
                           id,
                           'standard/update.html',
                           File,
                           FileUpdateForm,
                           'file:index',
                           None,
                           'doctris', _callback)


def delete(request, id):
    return standard_delete(request, id, File, 'file:index', {}, None)
