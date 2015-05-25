# -*- coding: utf-8 -*-

import requests


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


def run(code, webtask_token, method='POST'):
    wt_runner = WebtaskRunner(code, webtask_token)
    return wt_runner.run()
