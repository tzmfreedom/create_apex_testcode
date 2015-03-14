import re
import zipfile
import os
import sys

def isPythonVersionOver3():
    return sys.version_info >= (3, 0, 0)

if isPythonVersionOver3():
    import urllib.request
else:
    import urllib
    import urllib2

def httpRequest(method, endpoint, body, headers):
    if isPythonVersionOver3():
        if method == "POST":
            req = urllib.request.Request(url=endpoint, data=body.encode(), headers=headers)
            res = urllib.request.urlopen(req)
        elif method == "GET":
            url = endpoint
            if body != None:
                url += '?' + urllib.parse.urlencode(body)

            req = urllib.request.Request(url=url, headers=headers)
            res = urllib.request.urlopen(req)
        return res.read().decode()
    else:
        if method == "POST":
            req = urllib2.Request(url=endpoint, data=body, headers=headers)
            res = urllib2.urlopen(req)
        elif method == "GET":
            url = endpoint
            if body != None:
                url += '?' + urllib.urlencode(body)
            req = urllib2.Request(url=url, headers=headers)
            res = urllib2.urlopen(req)
        return res.read()

def getTextByTagName(tagname, target):
    p = re.compile(".+<" + tagname + ">(.+)</" + tagname + ">.+")
    m = p.match(target)
    return m.group(1)


def zip_write_dir(base_dir, src_dir, zip_name):
    zf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    current_dir = os.getcwd();
    os.chdir(base_dir)

    for root,dirs,files in os.walk(src_dir):
        for _file in files:
            filename = os.path.join(root,_file)
            arcname = filename
            zf.write(filename, arcname)

    zf.close()
    os.chdir(current_dir)

def multi_replace(target, replace_map):
    replaced_val = target
    for k, v in replace_map.items():
        replaced_val = replaced_val.replace(k, v)

    return replaced_val

def convert(val, field, described_field_map):
    type = described_field_map[field]['type']
    if type in ('id', 'string', 'reference', 'picklist', 'textarea', 'phone', 'email'):
        if val == None:
            return 'null'
        return "'" + val + "'";
    elif type == 'boolean':
        return 'true' if val else 'false'
    elif type in ('int', 'currency', 'double'):
        if val == None:
            return 'null'
        return str(val)
    elif type == 'datetime':
        return 'DateTime.now()'
    elif type == 'date':
        return 'Date.today()'
    else:
        return ''
