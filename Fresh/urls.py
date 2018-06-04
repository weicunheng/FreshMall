from django.conf.urls import url
from Fresh import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    # ---- 注册 ----
    url(r'^register/$',views.register),
    url(r'^user_isregister/$',views.user_isregister),
    url(r'^ajax_register/$',views.ajax_register),
]