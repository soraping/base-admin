#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: caoping
@file:   url.py
@time:   2020/09/29
@desc:
"""

from django.conf.urls import url
from .views import O2OUserListView

app_name = '[o2o]'

urlpatterns = [
    url(r'^list/', O2OUserListView.as_view(), name='o2o_list')
]