# coding:utf-8
import argparse
import util
import sf_util

VERSION = '30.0'
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-u','--username', required=True)
parser.add_argument('-p','--password', required=True)
parser.add_argument('-e','--environment')
parser.add_argument('-i','--id', required=True)
parser.add_argument('-n','--name')

args = parser.parse_args()

if args.environment == None:
    endpoint = "https://login.salesforce.com/services/Soap/u/{version}".format(version = VERSION)
else:
    endpoint = "https://test.salesforce.com/services/Soap/u/{version}".format(version = VERSION)

login_response = sf_util.login(args.username, args.password, endpoint)

prefix = args.id[0:3]
json_res = sf_util.describe_global(login_response, VERSION)
sobjects = json_res['sobjects']

for sobj in sobjects:
    if sobj['keyPrefix'] == prefix:
        json_res = sf_util.describe_sobject(login_response, sobj["name"], VERSION)
        res_fields = json_res['fields']
        fields = []
        described_fields = {}
        for field in res_fields:
            if field['createable']:
                described_fields[field['name']] = field
                fields.append(field['name'])
                
        json_res = sf_util.find_by_id(login_response, fields, sobj["name"], args.id, VERSION)
        
        obj_var = args.name if args.name != None else "obj"
        template = "{obj_var}.{field} = {value};"
        for field in fields:
            print(template.format(
                obj_var = obj_var,
                field = field,
                value = util.convert(json_res["records"][0][field], field, described_fields)
            ))