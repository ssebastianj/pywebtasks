# -*- coding: utf-8 -*-

from codecs import open

import requests

from .langs import JavaScript


class WebtaskRunner(object):
    def __init__(self, code, webtask_token, method='POST'):
        self._code = code
        self._webtask_token = webtask_token
        self._method = method

    def run(self):
        webtask_container = 'wt-ssebastianj-gmail_com-1'
        run_url = 'https://webtask.it.auth0.com/api/run/{}'.format(webtask_container)

        headers = {
            'Authorization': 'Bearer {}'.format(self._webtask_token),
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        return requests.post(run_url, data=self._code, headers=headers)


def run(code, webtask_token, lang=JavaScript, method='POST'):
    code_lang = lang()
    code = code_lang.template % code
    wt_runner = WebtaskRunner(code, webtask_token)
    return wt_runner.run()


def run_file(filepath, webtask_token, lang=JavaScript, method='POST'):
    code_string = ''
    with open(filepath, 'r', 'utf-8') as f:
        code_string = f.read()

    return run(code_string, webtask_token, lang, method)
