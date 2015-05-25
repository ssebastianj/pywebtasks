# -*- coding: utf-8 -*-

from codecs import open

import requests

from .langs import JavaScript


class WebtaskRunner(object):
    """Webtask Runner.
    """
    def __init__(self, code, container, webtask_token, url='', method='POST'):
        self._code = code
        self._container = container
        self._webtask_token = webtask_token
        self._url = url
        self._method = method

    def run(self):
        """Runs the webtask."""
        default_run_url = 'https://webtask.it.auth0.com/api/run/{}'.format(self._container)
        run_url = self._url or default_run_url

        headers = {
            'Authorization': 'Bearer {}'.format(self._webtask_token),
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        http_method = getattr(requests, self._method.lower())
        return http_method(run_url, data=self._code, headers=headers)


def run(code, container, webtask_token, url='', lang=JavaScript, method='POST'):
    """Runs a webtask from a string.

    :param code: String containing source code.
    :param container: Webtask container name in which webtask requests using
                      the newly issued token can execute code.
    :param webtask_token: Token required to execute webtasks with the API.
    :param url: URL of the API endpoint.
    :param lang: Classname which establishes the programming language to use.
    :param method: String of HTTP method to use for request the API.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    code_lang = lang()
    code = code_lang.template.format(code)
    wt_runner = WebtaskRunner(code, container, webtask_token, url, method)
    return wt_runner.run()


def run_file(filepath, container, webtask_token, url='', lang=JavaScript, method='POST'):
    """Runs a webtask from a source code file.

    :param filepath: Path to a source code file.
    :param container: Webtask container name in which webtask requests using
                      the newly issued token can execute code.
    :param webtask_token: Token required to execute webtasks with the API.
    :param url: URL of the API endpoint.
    :param lang: Classname which establishes the programming language to use.
    :param method: String of HTTP method to use for request the API.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    code_string = ''
    with open(filepath, 'r', 'utf-8') as f:
        code_string = f.read()

    return run(code_string, container, webtask_token, url, lang, method)
