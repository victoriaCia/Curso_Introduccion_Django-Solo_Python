from django.urls import path
from posts.views import (
    dummy_view,
    status_code_view,
    entry_list,
    redirect_back_home,
    MyClassView,
    MyListView
    )

app_name = 'posts'

urlpatterns = [
    path('', MyListView.as_view(), name='entry_list'),
    path('<id>/', dummy_view, name='entry_detail'),
    #path('(?P<id>[0-9]{4})/(?P<slug>[\w-]+)/$', dummy_view, name='entry_detail')   #url con expresiones regulares
    path('<id>/delete', dummy_view, name='entry_delete'),
    path('<id>/update', dummy_view, name='entry_update')
]