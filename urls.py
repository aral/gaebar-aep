# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from app1 import views as app1_views

urlpatterns = patterns('',
    # Example:
    # (r'^foo/', include('foo.urls')),

    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),

    url(r'^gaebar/', include('gaebar.urls')),
    url(r'^populate-datastore', view=app1_views.populate_datastore),
    url(r'^run-tests', view=app1_views.run_tests),
    url(r'', view=app1_views.index),
)
