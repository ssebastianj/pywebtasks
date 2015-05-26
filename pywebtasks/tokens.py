# -*- coding: utf-8 -*-

import json
import requests


def create(auth_token, container_name='', url='', notbefore_time=None,
           notafter_time=None, process_body=False, merge_body=False,
           max_depth=1, revoke_itself=False, protected_properties=None,
           encrypted_properties=None, container_limits=None,
           token_limits=None, **kwargs):

    properties = {}

    url = 'https://webtask.it.auth0.com/api/tokens/issue'
    headers = {
        'Authorization': 'Bearer {}'.format(auth_token),
        'Content-Type': 'application/json',
    }

    req = requests.post(url, data=json.dumps(properties), headers=headers)
    return req.content.decode('utf8')


def revoke(auth_token, token, **kwargs):
    """Revoke token.

    :param auth_token:
    :param token:
    :rtype: requests.Response.status_code
    """

    url = 'https://webtask.it.auth0.com/api/tokens/revoke'
    headers = {
        'Authorization': 'Bearer {}'.format(auth_token),
        'Content-Type': 'application/json',
    }

    payload = {'token': token}
    req = requests.post(url, data=json.dumps(payload), headers=headers)
    return req.status_code
