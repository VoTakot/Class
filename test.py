import requests

response = requests.get('http://127.0.0.1:8080/api/v2/users')
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')

response = requests.get('http://127.0.0.1:8080/api/v2/users')
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')

response = requests.get('http://127.0.0.1:8080/api/v2/users/1')
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')

response = requests.get('http://127.0.0.1:8080/api/v2/users/161')
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')

response = requests.post('http://127.0.0.1:8080/api/v2/users',
                         json={"collaborators": "3, 4", "end_date": null, "is_finished": false,
                               "job": "boom the asteroid", "start_date": null, "team_leader": 1, "work_size": 15))
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')

response = requests.post('http://127.0.0.1:8080/api/v2/users')
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')

response = requests.delete('http://127.0.0.1:8080/api/v2/users/142')
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')

response = requests.post('http://127.0.0.1:8080/api/v2/users/3')
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')