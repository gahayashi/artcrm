# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2015
@author: Gabriele Hayashi
'''
from pyramid.view import view_config, view_defaults


class BaseView(object):
    def __init__(self, request):
        self.request = request

class BaseAdminView(BaseView):
    pass

@view_defaults(route_name = 'web:root', renderer = 'root.jinja2')
class RootView(BaseView):
    @view_config(request_method = 'GET')
    def index(self):
        return {}
