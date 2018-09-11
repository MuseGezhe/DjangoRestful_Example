from django.conf.urls import url

from myApp import views

urlpatterns = [
    url(r'index/',views.index),

    # get和post请求
    url(r'students/$',views.studentsList),
    # get、put、patch、delete
    # ?P<xx>给参数命名，view里传的参数必须是xx
    url(r'students/(?P<pk>\d+)/$',views.studentDetail),

]
