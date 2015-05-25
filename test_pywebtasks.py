#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pywebtasks
----------------------------------

Tests for `pywebtasks` module.
"""

import os
import unittest

import pytest
import requests

from pywebtasks import compat
from pywebtasks import webtasks
from pywebtasks.webtasks import CSharpRunner
from pywebtasks.tokens import create_token, revoke_token

if compat.is_py3:
    def u(s):
        return s
else:
    def u(s):
        return s.decode('unicode-escape')

TEST_CODE_DIR = os.path.abspath(os.path.join('test_code'))
WEBTASK_TOKEN = os.environ.get('WEBTASK_TOKEN', '')


class WebtaskTokenTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_webtask_token_not_empty(self):
        assert WEBTASK_TOKEN != '', 'You must set the WEBTASK_TOKEN env variable'

    def test_create_token(self):
        webtask_token = create_token(WEBTASK_TOKEN)
        assert isinstance(webtask_token, str)
        assert webtask_token.split('.')[0] == WEBTASK_TOKEN.split('.')[0]

    def test_revoke_token(self):
        webtask_token = create_token(WEBTASK_TOKEN)
        status_code = revoke_token(WEBTASK_TOKEN, webtask_token)
        assert status_code == requests.codes.ok


class WebtaskTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_entry_points(self):
        webtasks.run
        webtasks.run_file

    def test_run_js_code_from_string(self):
        js_code = '''return function (context, cb) {
                        cb(null, "Hello, JS world!");
                     };
                  '''
        req = webtasks.run(js_code, WEBTASK_TOKEN)

        assert req.status_code == 200
        assert 'Hello, JS world!' in req.content.decode('utf-8')

    def test_run_js_code_from_file(self):
        js_code_filepath = os.path.join(TEST_CODE_DIR, 'javascript.js')
        req = webtasks.run_file(js_code_filepath, WEBTASK_TOKEN)

        assert req.status_code == 200
        assert 'Hello, JS world!' in req.content.decode('utf-8')

    def test_run_csharp_code_from_string(self):
        csharp_code = '''async (dynamic context) => {
                             return "Hello, C# world!";
                         }
                      '''
        req = webtasks.run(csharp_code, WEBTASK_TOKEN, CSharpRunner)

        assert req.status_code == 200
        assert 'Hello, C# world!' in req.content.decode('utf-8')

    def test_run_csharp_code_from_file(self):
        csharp_code_filepath = os.path.join(TEST_CODE_DIR, 'csharp.cs')
        req = webtasks.run_file(csharp_code_filepath,
                                WEBTASK_TOKEN,
                                CSharpRunner)

        assert req.status_code == 200
        assert 'Hello, C# world!' in req.content.decode('utf-8')

if __name__ == '__main__':
    unittest.main()
