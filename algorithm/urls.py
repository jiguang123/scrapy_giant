# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from handler import views

#urlpatterns = patterns('',
#    #  /handler/hisstock/twse
#
#    # ex: /handler/hisstock/twse/2317/20140808/20141111
#    url(r'^hisstock/(?P<hisdb>\w+)/(?P<stockid>\w+)/(?P<starttime>\d{8})/(?P<endtime>\d{8})/$',
#        view=views.hisstock_detail,
#        name='hisstock_detail'
#    ),
#