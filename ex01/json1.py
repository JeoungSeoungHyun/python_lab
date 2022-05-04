import json

print("="*60)
json_str = '''
{"id":1,"username":"cos","password":"1234"}
'''

# json -> dict
dic1 = json.loads(json_str)

print(dic1)
print(dic1["password"])

dit_to_json = json.dumps(dic1)

print(type(dit_to_json))
print(dit_to_json)
