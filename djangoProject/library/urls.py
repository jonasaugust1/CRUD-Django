from django.conf.urls import include
from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('livro_list/', livro_list, name='listar_livros'),
    path('livro_new/', livro_new, name='livro_new'),
    re_path('livro_edit/(?P<pk>[0-9]+)', livro_edit, name='livro_edit'),
    re_path('livro_delete/(?P<pk>[0-9]+)', livro_remove, name='livro_delete')
]