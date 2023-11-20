import json

mydict = {
    "opsco": [
        {
            "name": "PT. Moya Tangerang",
            "temperature": 30,
            "kelembapan": 75
        },
        {
            "name": "PT. Aetra Air Tangerang",
            "temperature": 28,
            "kelembapan": 74
        },
        {
            "name": "PT. Traya Tirta Cisadane",
            "temperature": 33,
            "kelembapan": 78
        },
        {
            "name": "PT. Tirta Kencana Cahaya Mandiri",
            "temperature": 38,
            "kelembapan": 79
        }
    ]
}

json_string = json.dumps(mydict, indent=4)
with open('mydata.json', 'w') as f:
    f.write(json_string)
