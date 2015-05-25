# -*- coding: utf-8 -*-

import json
import requests


def get_token_default_properties():
    token_properties = {}
    token_properties['ten'] = 'wt-ssebastianj-gmail_com-0'
    token_properties['nbf'] = 0
    token_properties['exp'] = 0
    token_properties['pb'] = 0
    token_properties['mb'] = 0
    token_properties['dp'] = 1
    token_properties['dr'] = 0
    token_properties['url'] = ''
    token_properties['pctx'] = {}
    token_properties['ectx'] = {}
    token_properties['ls'] = 0
    token_properties['lm'] = 0
    token_properties['lh'] = 0
    token_properties['ld'] = 0
    token_properties['lw'] = 0
    token_properties['lo'] = 0
    token_properties['lts'] = 0
    token_properties['ltm'] = 0
    token_properties['lth'] = 0
    token_properties['ltd'] = 0
    token_properties['ltw'] = 0
    token_properties['lto'] = 0
    return token_properties


def create_token(auth_token, container_name='', url='', notbefore_time=None,
                 notafter_time=None, process_body=False, merge_body=False,
                 max_depth=1, revoke_itself=False, protected_properties=None,
                 encrypted_properties=None, container_limits=None,
                 token_limits=None, **kwargs):

    properties = get_token_default_properties()




    url = 'https://webtask.it.auth0.com/api/tokens/issue'
    headers = {
        'Authorization': 'Bearer {}'.format(auth_token),
        'Content-Type': 'application/json',
    }

    req = requests.post(url, data=json.dumps(properties), headers=headers)
    return req.content.decode('utf8')


def revoke_token(auth_token, token, **kwargs):
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
    raise ValueError(req.request.body)
    return req.status_code
