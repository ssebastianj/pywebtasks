# -*- coding: utf-8 -*-

import json
import requests


def create_token(auth_token, container_name='', url='', notbefore_time=None,
                 notafter_time=None, process_body=False, merge_body=False,
                 max_depth=1, revoke_itself=False, protected_properties=None,
                 encrypted_properties=None, container_limits=None,
                 token_limits=None, **kwargs):

    properties = {}
    properties['ten'] = container_name
    properties['nbf'] = notbefore_time
    properties['exp'] = notafter_time
    properties['pb'] = int(process_body)
    properties['mb'] = int(merge_body)
    properties['dp'] = max_depth
    properties['dr'] = int(revoke_itself)
    properties['url'] = url

    if protected_properties is None:
        protected_properties = {}
    properties['pctx'] = protected_properties

    if encrypted_properties is None:
        encrypted_properties = {}
    properties['ectx'] = encrypted_properties

    if container_limits is not None:
        properties['ls'] = container_limits.get('second')
        properties['lm'] = container_limits.get('minute')
        properties['lh'] = container_limits.get('hour')
        properties['ld'] = container_limits.get('day')
        properties['lw'] = container_limits.get('week')
        properties['lo'] = container_limits.get('month')

    if token_limits is not None:
        properties['lts'] = token_limits.get('second')
        properties['ltm'] = token_limits.get('minute')
        properties['lth'] = token_limits.get('hour')
        properties['ltd'] = token_limits.get('day')
        properties['ltw'] = token_limits.get('week')
        properties['lto'] = token_limits.get('month')

    url = 'https://webtask.it.auth0.com/api/tokens/issue'
    headers = {
        'Authorization': 'Bearer {}'.format(auth_token),
        'Content-Type': 'application/json',
    }

    req = requests.post(url, data=json.dumps(properties), headers=headers)
    return req.content


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
    return req.status_code
