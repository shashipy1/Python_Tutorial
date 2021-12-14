import json

data = '{"var1": "SHASHI","var2": 56}'

# print(data['var1'])  -----------> string indices must be integers

skk = json.loads(data)
print(type(skk))
print(skk['var1'])

data2 = {
    "channel_name" : "SHASHICoder",
    "car" : ['bmw', 'audi a8', 'ferrari'],
    "fridge" : ('butter', 372),
    "isbad" : False
}

jscomp = json.dumps(data2)
print(jscomp)
