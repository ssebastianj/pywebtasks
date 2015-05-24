#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for PyWebtasks"""

import json
import os
import time
import unittest

import pytest

from pywebtasks import webtasks
from pywebtasks import compat
from pywebtasks.tokens import create_token, revoke_token

if compat.is_py3:
    def u(s):
        return s
else:
    def u(s):
        return s.decode('unicode-escape')


class WebtaskTokenTestCase(unittest.TestCase):
    def setUp(self):
        self.auth_token = os.environ.get('WEBTASK_AUTH_TOKEN')

        if self.auth_token is None:
            raise ValueError('You must set the WEBTASK_AUTH_TOKEN env variable.')

    def tearDown(self):
        pass

    def test_create_default_webtask_token(self):
        webtask_token = create_token(auth_token=self.auth_token)
        assert webtask_token is not None
        assert webtask_token != ''


if __name__ == '__main__':
    unittest.main()
