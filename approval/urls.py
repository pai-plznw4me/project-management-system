from django.urls import path
from approval.views import index, create, detail, update, delete, approval, not_approval

app_name='approval'
urlpatterns = [
    path('create/', create, name='create'),
    path('index/', index, name='index'),
    path('detail/<int:id>', detail, name='detail'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('approval/<int:id>', approval, name='approval'),
    path('not_approval/', not_approval, name='not_approval'),
]