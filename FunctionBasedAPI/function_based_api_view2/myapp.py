import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}

    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# get_data()  # Read data


def post_data():
    data = {
        'name': 'veeru',
        'roll': 104,
        'city': 'Ranchi',
    }
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# post_data()  # Create data


def update_data():
    data = {
        'id': 4,
        'name': 'Gajanan',
        'roll': '104',
        'city': 'Surat',
    }
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# update_data()  # Create data


def delete_data():
    data = {'id': 4}
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


delete_data()  # Delete data
