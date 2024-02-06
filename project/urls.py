from django.urls import path

from project.views import index, create, update, delete, detail, projectfile_create, projectfile_update, \
    projectfile_delete, projectfile_detail, projectfile_index

app_name='project'
urlpatterns=[
    path('index/', index, name='index'),
    # Project CRUD
    path('create/', create, name='create'),
    path('update/<str:id>', update, name='update'),
    path('delete/<str:id>', delete, name='delete'),
    path('detail/<str:id>', detail, name='detail'),
    # Projectfile CRUD
    path('projectfile/index/', projectfile_index, name='projectfile_index'),
    path('projectfile/create/', projectfile_create, name='projectfile_create'),
    path('projectfile/update/<str:id>', projectfile_update, name='projectfile_update'),
    path('projectfile/delete/<str:id>', projectfile_delete, name='projectfile_delete'),
    path('projectfile/detail/<str:id>', projectfile_detail, name='projectfile_detail'),

]