import json

j = {
    "employee":
        [
            {"id": 111, "name": "satoru"},
            {"id": 222, "name": "tarou"}
        ]
}

print(j)
print("#################")
print(json.dumps(j))

with open('test.json', 'w') as f:
    json.dump(j, f)

print("#########show by json.load ########")
with open('test.json', 'r') as f:
    print(json.load(f))
