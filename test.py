import requests


response = requests.post('http://127.0.0.1:8080/api/jobs/', json={
    "collaborators": "3, 4",
    "end_date": null,
    "is_finished": false,
    "job": "boom the asteroid",
    "start_date": null,
    "team_leader": 1,
    "work_size": 15
})
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')
response = requests.post('http://127.0.0.1:8080/api/jobs/', json={
    "collaborators": "3, 4",
    "end_date": null,
    "is_finished": false,
    "job": "boom the asteroid",
    "start_date": null,
    "team_leader": 'krutoi leader',
    "work_size": 15
})
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')
response = requests.post('http://127.0.0.1:8080/api/jobs/', json={
    "collaborators": "3, 4",
    "end_date": null,
    "is_finished": false,
    "job": "boom the asteroid",
    "start_date": null
})
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')
response = requests.post('http://127.0.0.1:8080/api/jobs/')
if response.status_code == 200:
    print(response.json())
else:
    print(f'{response.status_code} {response.reason}')