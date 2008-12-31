# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from app1 import views as app1_views

urlpatterns = patterns('',
    url(r'^gaebar/', include('gaebar.urls')),
    url(r'^populate-datastore', view=app1_views.populate_datastore),
    url(r'^run-tests', view=app1_views.run_tests),
    url(r'^flush', view=app1_views.flush_datastore),
    url(r'', view=app1_views.index),
)