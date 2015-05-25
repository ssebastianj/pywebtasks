# -*- coding: utf-8 -*-


class BaseLanguage(object):
    def __init__(self, name, extension='', template='{0}'):
        self.name = name
        self.extension = extension
        self.template = template


class JavaScript(BaseLanguage):
    def __init__(self):
        super(JavaScript, self).__init__('javascript', 'js')


class CSharp(BaseLanguage):
    def __init__(self):
        template = '''
            return function (cb) {{
                require('edge').func(function () {{/*
                {0}
                */}})(null, cb);
            }}
        '''
        super(CSharp, self).__init__('csharp', 'cs', template)
