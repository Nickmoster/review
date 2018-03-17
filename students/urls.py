from django.conf.urls import url
from .views import list,detail,index
urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^list/$',list,name='list'),
    # url(r"^detail/(\d+)/$",detail,name='detail'),
    url(r'^detail/(?P<id>\d+)/$',detail,name='detail'),
]