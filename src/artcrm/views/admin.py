# -*- coding: utf-8 -*-
'''
Created on Jan 23, 2015
@author: Gabriele Hayashi
'''
from pyramid.view import view_defaults, view_config

from artcrm.views.base import BaseAdminView


@view_defaults(route_name = 'web:admin', renderer = 'admin/index.jinja2')
class RootAdmin(BaseAdminView):
    @view_config(request_method = 'GET')
    def index(self):
        return {}