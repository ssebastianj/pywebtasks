# -*- coding: utf-8 -*-

import requests


class LanguageRunner(object):
    def __init__(self, name, extension='', template='%s'):
        self.name = name
        self.extension = extension
        self.template = template


class JavaScriptRunner(LanguageRunner):
    def __init__(self):
        super(JavaScriptRunner, self).__init__('javascript', 'js')


class CSharpRunner(LanguageRunner):
    def __init__(self):
        template = '''
            return function (cb) {
                require('edge').func(function () {/*
                %s
                */})(null, cb);
            }
        '''
        super(CSharpRunner, self).__init__('csharp', 'cs', template)


class WebtaskRunner(object):
    def __init__(self, code, webtask_token, method='POST'):
        self._code = code
        self._webtask_token = webtask_token
        self._method = method

    def run(self):
        webtask_container = 'wt-ssebastianj-gmail_com-0'
        run_url = 'https://webtask.it.auth0.com/api/run/{}'.format(webtask_container)

        headers = {
            'Authorization': 'Bearer {}'.format(self._webtask_token),
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        return requests.post(run_url, data=self._code, headers=headers)


def run(code, webtask_token, runner=JavaScriptRunner, method='POST'):
    code_runner = runner()
    code = code_runner.template % code
    wt_runner = WebtaskRunner(code, webtask_token)
    return wt_runner.run()


def run_file(filepath, webtask_token, runner=JavaScriptRunner, method='POST'):
    code_string = ''
    with open(filepath, 'r') as f:
        code_string = f.read()

    return run(code_string, webtask_token, runner, method)
