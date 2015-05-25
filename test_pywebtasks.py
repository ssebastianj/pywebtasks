#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for PyWebtasks"""

import json
import os
import time
import unittest

import pytest
import requests

from pywebtasks import webtasks
from pywebtasks import compat
from pywebtasks.tokens import create_token, revoke_token

if compat.is_py3:
    def u(s):
        return s
else:
    def u(s):
        return s.decode('unicode-escape')

TEST_CODE_DIR = os.path.abspath(os.path.join('test_code'))

WEBTASK_AUTH_TOKEN = os.environ.get('WEBTASK_AUTH_TOKEN', '')


class WebtaskTokenTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_webtask_token_not_empty(self):
        assert WEBTASK_AUTH_TOKEN != '', 'You must set the WEBTASK_AUTH_TOKEN env variable'

    def test_create_token(self):
        webtask_token = create_token(WEBTASK_AUTH_TOKEN)
        assert isinstance(webtask_token, str)
        assert webtask_token.split('.')[0] == WEBTASK_AUTH_TOKEN.split('.')[0]

    def test_revoke_token(self):
        webtask_token = create_token(WEBTASK_AUTH_TOKEN)
        status_code = revoke_token(WEBTASK_AUTH_TOKEN, webtask_token)
        assert status_code == requests.codes.ok


class WebtaskTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_entry_points(self):
        webtasks.run

    def test_run_code_js_code_ok(self):
        js_code = ''
        with open(os.path.join(TEST_CODE_DIR, 'javascript.js')) as f:
            js_code = f.read()

        req = webtasks.run(js_code, WEBTASK_AUTH_TOKEN)
        assert req.status_code == 200
        assert 'Hello, JS world!' in req.content.decode('utf-8')

    def test_run_code_csharp_code_ok(self):
        csharp_code = ''
        with open(os.path.join(TEST_CODE_DIR, 'csharp.cs')) as f:
            csharp_code = f.read()

        js_code = '''
            return function (context, cb) {
                require('edge').func(function () {
                    /* %s */
                })(null, cb);
            }
            ''' % csharp_code

        req = webtasks.run(js_code, WEBTASK_AUTH_TOKEN)
        assert req.status_code == 200
        assert 'Hello, C# world!' in req.content.decode('utf-8')

if __name__ == '__main__':
    unittest.main()
