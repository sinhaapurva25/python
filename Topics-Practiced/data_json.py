import json
with open(r'data.json') as d:
    data = json.load(d)
print(data)

data2 = {
    "init":
    {
      "qwerty": 78,
      "rtyu": 90
    }
}
with open('data2.json','w') as d:
    json.dump(data2,d)