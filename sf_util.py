import util
import os
import time
import base64
import re
import const
import json

def login(username, password, endpoint):
    login_body = const.LOGIN_BODY.format(
        username = username,
        password = password
    )
    res = util.httpRequest("POST", endpoint, login_body, const.SOAP_HEADER)

    server_url = util.getTextByTagName("serverUrl", res)
    p = re.compile("^(https:\/\/.+?\.salesforce\.com)\/")
    m = p.match(server_url)
    base_url = m.group(1)

    return {
        "session_id" : util.getTextByTagName("sessionId", res),
        "base_url" : base_url
    }

def describe_global(login_response, version):
    request_url = '{base_url}/services/data/v{version}/sobjects/'.format(
        base_url = login_response["base_url"],
        version = version
    )
    res = util.httpRequest(
        "GET",
        request_url,
        None,
        {
            "Authorization" : "Bearer " + login_response["session_id"]
        }
    )
    return json.loads(res)

def describe_sobject(login_response, sobject_name, version = '30.0'):
    request_url = "{base_url}/services/data/v{version}/sobjects/{sobject}/describe/".format(
        base_url = login_response["base_url"],
        version = version,
        sobject = sobject_name
    )
    res = util.httpRequest(
        "GET",
        request_url,
        None,
        {
            "Authorization" : "Bearer " + login_response["session_id"]
        }
    )
    return json.loads(res)

def find_by_id(login_response, fields, sobject_name, id, version = '30.0'):
    query = "SELECT {fields} FROM {sobject} WHERE id = '{id}'".format(
        fields = ",".join(fields),
        sobject = sobject_name,
        id = id
    )

    request_url = '{base_url}/services/data/v{version}/query/'.format(
        base_url = login_response["base_url"],
        version = version
    )
    res = util.httpRequest(
        "GET",
        request_url,
        {
            'q' : query
        },
        {
            "Authorization" : "Bearer " + login_response["session_id"]
        }
    )
    return json.loads(res)
